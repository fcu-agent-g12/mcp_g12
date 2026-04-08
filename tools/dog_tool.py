"""
Tool：取得隨機狗狗圖片

每日一狗：呼叫 Dog CEO API，回傳一張隨機狗狗圖片的 URL。
"""

import requests

TOOL_INFO = {
    "name": "get_dog_image",
    "api": "https://dog.ceo/api/breeds/image/random",
    "author": "你的名字",
}


def get_dog_image_data() -> str:
    """呼叫 Dog CEO API，回傳隨機狗狗圖片 URL"""
    resp = requests.get("https://dog.ceo/api/breeds/image/random", timeout=10)
    resp.raise_for_status()
    return resp.json()["message"]


# 單獨測試
if __name__ == "__main__":
    print(get_dog_image_data())
