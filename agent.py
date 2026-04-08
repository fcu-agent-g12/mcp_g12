import asyncio
import os
from typing import Any
from google import genai
from google.genai import types
from mcp.client.sse import sse_client
from mcp.client.session import ClientSession
from dotenv import load_dotenv

# 加載環境變數
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = "gemini-2.5-flash"  # 使用使用者環境中可用的新版

# 初始化 Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

async def run_agent():
    print(f"🚀 正在連接到 MCP Server...")
    
    # 1. 使用 MCP SSE Client 連接到 server.py
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化 MCP Session
            await session.initialize()
            
            # 2. 自動取得 Server 提供的所有工具清單
            tools_response = await session.list_tools()
            mcp_tools = tools_response.tools
            
            # 3. 把工具清單轉換成 Gemini API 的 function declaration 格式
            declarations = []
            for tool in mcp_tools:
                declarations.append(types.FunctionDeclaration(
                    name=tool.name,
                    description=tool.description,
                    parameters=tool.inputSchema
                ))
            
            # 建立 Gemini 工具集
            gemini_tools = [types.Tool(function_declarations=declarations)]
            
            print(f"✅ 已連接！載入了 {len(declarations)} 個工具。")
            print("💡 您可以開始跟我對話了（輸入 'exit' 退出）。")

            # 4. 進行多輪對話
            config = types.GenerateContentConfig(
                tools=gemini_tools,
                system_instruction="你是一位親切的每日生活智慧助手。你可以幫使用者查詢天氣、提供今日金句或健康建議。"
            )
            chat = client.chats.create(model=MODEL_ID, config=config)

            while True:
                user_input = input("\n👤 您：")
                if user_input.lower() in ["exit", "退出", "bye"]:
                    break
                
                # 發送訊息給 Gemini
                try:
                    response = chat.send_message(user_input)
                except Exception as e:
                    print(f"❌ Gemini API 呼叫失敗：{str(e)}")
                    continue
                
                # 5. 處理 Gemini 的回應（包含 Function Call）
                while response.candidates and response.candidates[0].content.parts[0].function_call:
                    for part in response.candidates[0].content.parts:
                        if part.function_call:
                            fn_call = part.function_call
                            fn_name = fn_call.name
                            args = fn_call.args
                            
                            # 10. Debug 輸出（調用工具的過程）
                            print(f"🔍 [DEBUG] Agent 正在呼叫工具：{fn_name}，參數：{args}")
                            
                            # 透過 MCP call_tool 呼叫對應的 Tool
                            try:
                                tool_result = await session.call_tool(fn_name, args)
                                # 把結果送回 Gemini 繼續對話
                                print(f"📥 [DEBUG] 工具回傳結果：{tool_result.content[0].text}")
                                
                                response = chat.send_message(
                                    types.Part.from_function_response(
                                        name=fn_name,
                                        response={"result": tool_result.content[0].text}
                                    )
                                )
                            except Exception as e:
                                print(f"❌ 呼叫 MCP Tool {fn_name} 失敗：{str(e)}")
                                # 回傳錯誤給 Gemini 讓它知道
                                response = chat.send_message(
                                    types.Part.from_function_response(
                                        name=fn_name,
                                        response={"error": str(e)}
                                    )
                                )
                
                # 6. 當 Gemini 回傳文字時，直接顯示
                if response.text:
                    print(f"🤖 助手：{response.text}")

if __name__ == "__main__":
    try:
        asyncio.run(run_agent())
    except KeyboardInterrupt:
        print("\n👋 再見！")
    except Exception as e:
        print(f"❌ 發生錯誤：{str(e)}")
