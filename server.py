"""
W8 分組實作：MCP Server
主題：每日生活顧問 (Daily Life Advisor)
"""

from mcp.server.fastmcp import FastMCP
from tools.weather_tool import get_weather_data
from tools.quote_tool import get_quote_data

mcp = FastMCP("Group-12-Advisor")


# ════════════════════════════════
#  Tools：核心功能工具
# ════════════════════════════════

@mcp.tool()
def get_quote() -> str:
    """獲取今日金句或活動建議。
    當使用者想要一點靈感或不知道要做什麼時使用。"""
    return get_quote_data()


@mcp.tool()
def get_weather(city: str) -> str:
    """取得指定城市的即時天氣資訊。
    當使用者詢問天氣、溫度、適合的活動時使用。"""
    return get_weather_data(city)

@mcp.tool()
def hello(name: str) -> str:
    """跟使用者打招呼。測試用，確認 MCP Server 正常運作。"""
    return f"你好，{name}！我是您的第 12 組每日生活顧問。MCP Server 運作正常 🎉"


# ════════════════════════════════
#  Resource：提供靜態參考資料
# ════════════════════════════════

@mcp.resource("info://healthy-habits")
def get_healthy_habits() -> str:
    """每日健康生活建議清單"""
    return (
        "每日健康習慣：\n"
        "- 起床後喝一杯溫開水\n"
        "- 每小時站起來活動 5 分鐘\n"
        "- 午餐後散步 10 分鐘\n"
        "- 睡前 30 分鐘遠離螢幕\n\n"
        "飲食建議：\n"
        "- 每天攝取 5 種不同顏色的蔬果\n"
        "- 減少加工食品和含糖飲料\n"
        "- 細嚼慢嚥，專心吃飯"
    )


# ════════════════════════════════
#  Prompt：整合多個 Tool 的提示詞模板
# ════════════════════════════════

@mcp.prompt()
def plan_my_day(city: str) -> str:
    """產生每日生活計畫的提示詞"""
    return (
        f"請幫我規劃今天的生活：\n"
        f"1. 查詢 {city} 的天氣，判斷適合室內還是室外活動\n"
        f"2. 根據天氣推薦 3 個今天可以做的活動\n"
        f"3. 給我今日一笑和一則人生建議\n"
        f"4. 給我一則有趣的冷知識當作今日小知識\n"
        f"請用繁體中文，語氣親切活潑。"
    )


if __name__ == "__main__":
    print("MCP Server 啟動中... http://localhost:8000")
    mcp.run(transport="sse")
