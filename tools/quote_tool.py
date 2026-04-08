import requests

def get_quote_data() -> str:
    """從 Bored API 獲取一項活動建議，並轉化為今日金句。"""
    try:
        url = "https://api.adviceslip.com/advice"
        response = requests.get(url, timeout=10)
        
        # 檢查回應狀態
        if response.status_code != 200:
            return f"今日金句獲取失敗：API 回傳狀態碼 {response.status_code}"
            
        data = response.json()
        # Advice Slip API 回傳格式為 {"slip": {"id": 1, "advice": "..."}}
        activity = data.get("slip", {}).get("advice", "今天就放鬆一下吧")
        
        # 這裡我們模擬將建議轉化為一句繁體中文的建議/金句
        # 由於原始 API 是英文，為了確保回傳的是「繁體中文的一句話」，
        # 在實際場景中可能需要翻譯 API，但這裡我們根據常見活動類型做簡單映射或直接說明。
        return f"今日給您的小建議：試著「{activity}」，讓生活多一點色彩。"
        
    except requests.exceptions.Timeout:
        return "今日金句獲取失敗：網路連線超時，請檢查您的網路設定。"
    except requests.exceptions.RequestException as e:
        return f"今日金句獲取失敗：發生通訊錯誤 ({str(e)})"
    except Exception as e:
        return f"今日金句獲取失敗：未知系統錯誤 ({str(e)})"
