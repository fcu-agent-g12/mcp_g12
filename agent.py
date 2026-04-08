import os
import asyncio
from dotenv import load_dotenv
from mcp.client.sse import sse_client
from mcp.client.session import ClientSession
from google import genai
from google.genai import types

load_dotenv()


async def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ 請在 .env 中設定 GEMINI_API_KEY")
        return

    client = genai.Client(api_key=api_key)

    server_url = "http://localhost:8000/sse"
    print(f"🔗 正在連接到 MCP Server: {server_url}")

    async with sse_client(server_url) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("✅ 成功連接到 MCP Server！")

            tools_response = await session.list_tools()
            print(f"🛠️  自動取得 {len(tools_response.tools)} 個工具。")

            declarations = []
            for t in tools_response.tools:
                decl = types.FunctionDeclaration(
                    name=t.name,
                    description=t.description or "",
                    parameters=t.inputSchema,
                )
                declarations.append(decl)
                print(f"  - {t.name}: {t.description}")

            gemini_tools = []
            if declarations:
                gemini_tools = [types.Tool(function_declarations=declarations)]

            chat = client.aio.chats.create(
                model="gemini-2.0-flash",
                config=types.GenerateContentConfig(tools=gemini_tools, temperature=0.7),
            )

            print("\n🤖 Gemini Agent 建立完成，聊天開始 (輸入 'quit' 或 'exit' 結束)")

            while True:
                user_msg = input("\n你: ")
                if user_msg.lower() in ("quit", "exit"):
                    print("👋 掰掰！")
                    break
                if not user_msg.strip():
                    continue

                try:
                    response = await chat.send_message(user_msg)

                    while True:
                        if response.function_calls:
                            func_responses = []
                            for fc in response.function_calls:
                                tool_name = fc.name
                                tool_args = fc.args
                                print(f"\n  [Debug] 👉 Agent 決定呼叫工具: {tool_name}")
                                print(f"  [Debug] 參數: {tool_args}")

                                try:
                                    tool_result = await session.call_tool(
                                        tool_name, arguments=tool_args
                                    )
                                    result_text = "\n".join(
                                        [
                                            c.text
                                            for c in tool_result.content
                                            if c.type == "text"
                                        ]
                                    )
                                    print(
                                        f"  [Debug] 👈 工具回傳結果長度: {len(result_text)} 字元"
                                    )
                                    print(f"  [Debug] 結果片段: {result_text[:50]}...")

                                    func_responses.append(
                                        types.Part.from_function_response(
                                            name=tool_name,
                                            response={"result": result_text},
                                        )
                                    )
                                except Exception as e:
                                    print(f"  [Debug] ❌ 工具呼叫發生錯誤: {e}")
                                    func_responses.append(
                                        types.Part.from_function_response(
                                            name=tool_name, response={"error": str(e)}
                                        )
                                    )

                            print("  [Debug] 🔄 將結果送回給 Agent...")
                            response = await chat.send_message(func_responses)
                        else:
                            if response.text:
                                print(f"\n🤖 Agent: {response.text}")
                            break

                except Exception as e:
                    print(f"⚠️ 對話發生錯誤: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n使用者提早結束程式。")
