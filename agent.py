"""
W8 分組實作：MCP Client + Gemini Agent
使用 MCP SSE Client 連接 Server，搭配 Gemini 2.0 Flash 進行多輪對話。
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

# ── 載入環境變數 ────────────────────────────────────────────────────────────
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("請在 .env 檔案中設定 GEMINI_API_KEY")

MCP_SERVER_URL = "http://localhost:8000/sse"
MODEL_ID = "gemini-2.0-flash"

# ── 工具格式轉換：MCP → Gemini FunctionDeclaration ──────────────────────────

def mcp_tool_to_gemini(tool) -> types.FunctionDeclaration:
    """把 MCP Tool 物件轉成 Gemini FunctionDeclaration。"""
    # 取出 inputSchema，若沒有則給空 object schema
    input_schema = getattr(tool, "inputSchema", None) or {}

    # Gemini 需要 type + properties 結構
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


# ── 主要 Agent 邏輯 ─────────────────────────────────────────────────────────

async def run_agent():
    print("=" * 55)
    print("  MCP + Gemini Agent 啟動中")
    print(f"  連接至：{MCP_SERVER_URL}")
    print("=" * 55)

    # 1. 建立 MCP SSE 連線
    async with sse_client(MCP_SERVER_URL) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("[MCP] 連線成功，正在取得工具清單…\n")

            # 2. 取得工具清單
            tools_response = await session.list_tools()
            mcp_tools = tools_response.tools
            print(f"[MCP] 共取得 {len(mcp_tools)} 個工具：")
            for t in mcp_tools:
                print(f"      • {t.name}：{t.description}")
            print()

            # 3. 轉換成 Gemini 格式
            gemini_tools = [types.Tool(
                function_declarations=[mcp_tool_to_gemini(t) for t in mcp_tools]
            )]

            # 4. 初始化 Gemini 客戶端
            client = genai.Client(api_key=GEMINI_API_KEY)

            # 對話歷史（多輪）
            history: list[types.Content] = []

            print("輸入 'exit' 或 'quit' 結束對話。")
            print("-" * 55)

            # 5. 多輪對話迴圈
            while True:
                # 取得使用者輸入
                try:
                    user_input = input("\n你：").strip()
                except (EOFError, KeyboardInterrupt):
                    print("\n[Agent] 對話結束。")
                    break

                if not user_input:
                    continue
                if user_input.lower() in {"exit", "quit"}:
                    print("[Agent] 對話結束。")
                    break

                # 加入使用者訊息到歷史
                history.append(types.Content(
                    role="user",
                    parts=[types.Part(text=user_input)],
                ))

                # 內部迴圈：讓 Gemini 可以連續呼叫工具直到給出最終回答
                while True:
                    # 呼叫 Gemini，遇到 429 自動等待重試
                    for attempt in range(5):
                        try:
                            response = client.models.generate_content(
                                model=MODEL_ID,
                                contents=history,
                                config=types.GenerateContentConfig(
                                    tools=gemini_tools,
                                ),
                            )
                            break  # 成功就跳出重試迴圈
                        except Exception as e:
                            err_str = str(e)
                            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                                # 從錯誤訊息解析建議等待秒數
                                match = re.search(r"retry in ([\d.]+)s", err_str)
                                wait_sec = float(match.group(1)) if match else 30
                                wait_sec = min(wait_sec + 5, 60)  # 多等 5 秒緩衝
                                print(f"\n[WARN] API 配額限制，等待 {wait_sec:.0f} 秒後重試（第 {attempt+1}/5 次）...")
                                time.sleep(wait_sec)
                            else:
                                raise  # 其他錯誤直接拋出
                    else:
                        print("[ERROR] 已達最大重試次數，跳過此輪對話。")
                        break

                    candidate = response.candidates[0]
                    content = candidate.content  # types.Content (role=model)
                    history.append(content)      # 加入模型回應到歷史

                    # 檢查是否有 function_call
                    function_calls = [
                        part for part in content.parts
                        if part.function_call is not None
                    ]

                    if function_calls:
                        # 6. 呼叫對應的 MCP Tool
                        tool_result_parts = []
                        for part in function_calls:
                            fc = part.function_call
                            tool_name = fc.name
                            tool_args = dict(fc.args) if fc.args else {}

                            print(f"\n[DEBUG] 呼叫工具：{tool_name}")
                            print(f"[DEBUG] 參數：{json.dumps(tool_args, ensure_ascii=False)}")

                            mcp_result = await session.call_tool(tool_name, tool_args)

                            # 取出回傳文字
                            result_text = ""
                            for block in mcp_result.content:
                                if hasattr(block, "text"):
                                    result_text += block.text

                            print(f"[DEBUG] 結果：{result_text}")

                            tool_result_parts.append(
                                types.Part(
                                    function_response=types.FunctionResponse(
                                        name=tool_name,
                                        response={"result": result_text},
                                    )
                                )
                            )

                        # 把工具結果送回 Gemini
                        history.append(types.Content(
                            role="user",
                            parts=tool_result_parts,
                        ))
                        # 繼續內部迴圈，讓 Gemini 消化工具結果

                    else:
                        # 6. Gemini 給出文字回答，結束內部迴圈
                        text_parts = [
                            p.text for p in content.parts if p.text
                        ]
                        final_text = "".join(text_parts).strip()
                        print(f"\nGemini：{final_text}")
                        break  # 跳出內部迴圈，等待下一輪使用者輸入


# ── 入口 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    asyncio.run(run_agent())
