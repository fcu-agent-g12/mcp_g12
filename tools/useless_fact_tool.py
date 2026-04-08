"""
今日冷知識 Tool

呼叫 https://uselessfacts.jsph.pl/api/v2/facts/random
取得一則隨機英文冷知識，並附上來源連結。
"""

import requests

# Tool 資訊（給人看的，不影響 MCP）
TOOL_INFO = {
    "name": "get_fun_fact",
    "api": "https://uselessfacts.jsph.pl/api/v2/facts/random",
    "author": "第12組",
}

API_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"


def get_fun_fact_data() -> str:
    """
    呼叫 Useless Facts API，回傳一則隨機冷知識（英文）及來源連結。
    """
    resp = requests.get(API_URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    fact_text = data.get("text", "（無法取得冷知識）")
    source_url = data.get("source_url", "")
    permalink = data.get("permalink", "")

    result = f"今日冷知識：{fact_text}"
    if source_url:
        result += f"\n來源：{source_url}"
    if permalink:
        result += f"\n永久連結：{permalink}"

    return result


# 單獨測試
if __name__ == "__main__":
    print(get_fun_fact_data())
