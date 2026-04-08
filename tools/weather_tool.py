"""
天氣查詢 Tool

呼叫 https://wttr.in/{city}?format=j1
取得指定城市的即時天氣資訊，包含溫度、體感溫度、濕度、風速與天氣描述。
"""

import requests

# Tool 資訊（給人看的，不影響 MCP）
TOOL_INFO = {
    "name": "get_weather",
    "api": "https://wttr.in/{city}?format=j1",
    "author": "第12組",
}

API_URL = "https://wttr.in/{city}?format=j1"


def get_weather_data(city: str) -> str:
    """
    呼叫 wttr.in API，回傳指定城市的即時天氣資訊。

    Args:
        city: 城市名稱，例如 "Taipei"、"Tokyo"、"London"

    Returns:
        包含天氣描述、溫度、濕度、風速等資訊的字串
    """
    url = API_URL.format(city=city)
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # 取得第一個天氣觀測資料
    current = data.get("current_condition", [{}])[0]

    # 天氣描述（英文）
    desc_list = current.get("weatherDesc", [{}])
    description = desc_list[0].get("value", "未知") if desc_list else "未知"

    # 溫度（攝氏）
    temp_c = current.get("temp_C", "N/A")
    feels_like_c = current.get("FeelsLikeC", "N/A")

    # 濕度
    humidity = current.get("humidity", "N/A")

    # 風速（km/h）
    wind_speed = current.get("windspeedKmph", "N/A")
    wind_dir = current.get("winddir16Point", "N/A")

    # 能見度
    visibility = current.get("visibility", "N/A")

    # 降雨機率（來自預報的第一個時段）
    hourly = data.get("weather", [{}])[0].get("hourly", [{}])
    rain_chance = hourly[0].get("chanceofrain", "N/A") if hourly else "N/A"

    # 是否建議帶傘
    umbrella_advice = "建議帶傘" if str(rain_chance) not in ("N/A", "0") and int(rain_chance) >= 30 else "不需帶傘"

    result = (
        f"[天氣] {city} 即時天氣\n"
        f"{'-' * 30}\n"
        f"天氣狀況：{description}\n"
        f"氣溫：{temp_c} C（體感 {feels_like_c} C）\n"
        f"濕度：{humidity}%\n"
        f"風速：{wind_speed} km/h（{wind_dir}）\n"
        f"能見度：{visibility} km\n"
        f"降雨機率：{rain_chance}%\n"
        f"帶傘建議：{umbrella_advice}"
    )

    return result


# 單獨測試
if __name__ == "__main__":
    print(get_weather_data("Taipei"))
