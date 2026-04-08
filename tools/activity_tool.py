import requests

def get_activity_data() -> str:
    """呼叫 Bored API，回傳一則隨機活動建議"""
    try:
        # 注意：Appbrewery 的 Bored API 回傳格式為 {"activity": "...", "type": "...", ...}
        resp = requests.get("https://bored-api.appbrewery.com/random", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        activity = data.get("activity", "沒有取得活動")
        category = data.get("type", "未知")
        
        return f"推薦活動：{activity} (類型：{category})"
    except Exception as e:
        return f"目前無法取得活動建議，錯誤：{str(e)}"

# 單獨測試用
if __name__ == "__main__":
    print(get_activity_data())