"""
範例 Tool：取得天氣資訊

這是一個取得天氣資訊的簡單 Tool。
"""

import requests

# Tool 資訊（給人看的，不影響 MCP）
TOOL_INFO = {
    "name": "get_weather",
    "api": "https://wttr.in",
    "author": "TyrantRey",
}


def get_weather_data(city: str = "Taipei") -> dict:
    """呼叫 wttr.in API，回傳指定地點的 JSON 格式天氣資訊"""
    url = f"https://wttr.in/{city}?format=j1"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()


# 單獨測試
if __name__ == "__main__":
    import json
    # 印出排版後的 JSON
    print(json.dumps(get_weather_data(), indent=2, ensure_ascii=False))
