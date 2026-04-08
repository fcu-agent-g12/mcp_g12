import requests

def get_weather_data(city: str) -> str:
    """获取指定城市的即时天气资讯。
    使用 wttr.in 提供的 API。"""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['lang_zh'][0]['value'] if 'lang_zh' in current else current['weatherDesc'][0]['value']
        humidity = current['humidity']
        
        return f"{city} 目前天气：{desc}\n温度：{temp}°C\n湿度：{humidity}%"
    except Exception as e:
        return f"查询 {city} 天气时发生错误：{str(e)}"
