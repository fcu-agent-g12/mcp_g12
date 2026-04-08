"""
自動測試腳本：不需要使用者輸入，自動送出問題並顯示結果。
"""

import asyncio
import json
import os
import re
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from mcp import ClientSession
from mcp.client.sse import sse_client

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MCP_SERVER_URL = "http://localhost:8000/sse"
MODEL_ID = "gemini-2.0-flash"

# ── 預設自動執行的問題清單 ───────────────────────────────────────────────────
AUTO_QUESTIONS = [
    "給我一則今日冷知識",
    "再給我一則有趣的冷知識",
]


def mcp_tool_to_gemini(tool) -> types.FunctionDeclaration:
    input_schema = getattr(tool, "inputSchema", None) or {}
    parameters = None
    if input_schema:
        parameters = types.Schema(
            type=input_schema.get("type", "object"),
            properties={
                name: types.Schema(
                    type=prop.get("type", "string"),
                    description=prop.get("description", ""),
                )
                for name, prop in input_schema.get("properties", {}).items()
            },
            required=input_schema.get("required", []),
        )
    return types.FunctionDeclaration(
        name=tool.name,
        description=tool.description or "",
        parameters=parameters,
    )


def call_gemini_with_retry(client, model_id, history, gemini_tools, max_retries=5):
    """呼叫 Gemini，遇到 429 自動等待重試。"""
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=history,
                config=types.GenerateContentConfig(tools=gemini_tools),
            )
            return response
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                match = re.search(r"retry in ([\d.]+)s", err_str)
                wait_sec = float(match.group(1)) if match else 30
                wait_sec = min(wait_sec + 5, 65)
                print(f"  [WARN] 配額限制，{wait_sec:.0f} 秒後重試（{attempt+1}/{max_retries}）...")
                time.sleep(wait_sec)
            else:
                raise
    raise RuntimeError("已達最大重試次數，API 仍無法回應。")


async def run_auto_test():
    print("=" * 55)
    print("  MCP + Gemini 自動測試")
    print(f"  Server：{MCP_SERVER_URL}")
    print("=" * 55)

    async with sse_client(MCP_SERVER_URL) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools_response = await session.list_tools()
            mcp_tools = tools_response.tools
            print(f"[MCP] 取得 {len(mcp_tools)} 個工具：{[t.name for t in mcp_tools]}\n")

            gemini_tools = [types.Tool(
                function_declarations=[mcp_tool_to_gemini(t) for t in mcp_tools]
            )]
            client = genai.Client(api_key=GEMINI_API_KEY)

            for i, question in enumerate(AUTO_QUESTIONS, 1):
                print(f"{'─'*55}")
                print(f"[問題 {i}] {question}")
                print(f"{'─'*55}")

                history = [types.Content(
                    role="user",
                    parts=[types.Part(text=question)],
                )]

                while True:
                    response = call_gemini_with_retry(client, MODEL_ID, history, gemini_tools)
                    candidate = response.candidates[0]
                    content = candidate.content
                    history.append(content)

                    function_calls = [p for p in content.parts if p.function_call is not None]

                    if function_calls:
                        tool_result_parts = []
                        for part in function_calls:
                            fc = part.function_call
                            tool_name = fc.name
                            tool_args = dict(fc.args) if fc.args else {}
                            print(f"  [TOOL] 呼叫：{tool_name}  參數：{json.dumps(tool_args, ensure_ascii=False)}")

                            mcp_result = await session.call_tool(tool_name, tool_args)
                            result_text = "".join(
                                block.text for block in mcp_result.content if hasattr(block, "text")
                            )
                            print(f"  [TOOL] 結果：{result_text}\n")

                            tool_result_parts.append(types.Part(
                                function_response=types.FunctionResponse(
                                    name=tool_name,
                                    response={"result": result_text},
                                )
                            ))
                        history.append(types.Content(role="user", parts=tool_result_parts))
                    else:
                        final_text = "".join(p.text for p in content.parts if p.text).strip()
                        print(f"  [Gemini] {final_text}\n")
                        break

    print("=" * 55)
    print("  自動測試完成！")
    print("=" * 55)


if __name__ == "__main__":
    asyncio.run(run_auto_test())
