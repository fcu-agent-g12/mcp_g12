# MCP Server + AI agent 分組實作

> 課程：AI Agent 開發 — MCP（Model Context Protocol）
> 主題：（填入你們選的主題）

---

## Server 功能總覽

> 說明這個 MCP Server 提供哪些 Tool

| Tool 名稱   | 功能說明     | 負責組員 |
| ----------- | ------------ | -------- |
| get_weather | 查詢即時天氣 | 張紹謙   |
|             |              |          |
|             |              |          |

---

## 組員與分工

| 姓名   | 負責功能            | 檔案        | 使用的 API                       |
| ------ | ------------------- | ----------- | -------------------------------- |
| 張紹謙 | get_weather         | `tools/`    | https://wttr.in/{city}?format=j1 |
|        |                     | `tools/`    |                                  |
|        |                     | `tools/`    |                                  |
| 張紹謙 | Resource + Prompt   | `server.py` | —                                |
|        | Agent（用 AI 產生） | `agent.py`  | Gemini API                       |

---

## 專案架構

```
├── server.py              # MCP Server 主程式
├── agent.py               # MCP Client + Gemini Agent（用 AI 產生）
├── tools/
│   ├── __init__.py
│   ├── example_tool.py    # 範例（可刪除）
│   ├── xxx_tool.py        # 組員 A 的 Tool
│   ├── xxx_tool.py        # 組員 B 的 Tool
│   └── xxx_tool.py        # 組員 C 的 Tool
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 使用方式

```bash
# 1. 建立虛擬環境
python3 -m venv .venv
source .venv/bin/activate

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 設定 API Key
cp .env.example .env
# 編輯 .env，填入你的 GEMINI_API_KEY

# 4. 用 MCP Inspector 測試 Server
mcp dev server.py

# 5. 用 Agent 對話
python agent.py
```

---

## 測試結果

### MCP Inspector 截圖

> 貼上 Inspector 的截圖（Tools / Resources / Prompts 三個分頁都要有）

### Agent 對話截圖

> 貼上 Agent 對話的截圖（顯示 Gemini 呼叫 Tool 的過程，以及使用 /use 呼叫 Prompt 的結果）

---

## 各 Tool 說明

### `get_weather`（負責：張紹謙）

- **功能**：取得指定城市的即時天氣資訊。
- **使用 API**：https://wttr.in/{city}?format=j1
- **參數**：city: str
- **回傳範例**：

```json
{
  "current_condition": [
    {
      "FeelsLikeC": "-2",
      "FeelsLikeF": "29",
      "cloudcover": "0",
      "humidity": "74",
      "localObsDateTime": "2026-04-08 05:15 AM",
      "observation_time": "03:15 AM",
      "precipInches": "0.0",
      "precipMM": "0.0",
      "pressure": "1029",
      "pressureInches": "30",
      "temp_C": "-1",
      "temp_F": "30",
      "uvIndex": "0",
      "visibility": "10",
      "visibilityMiles": "6",
      "weatherCode": "113",
      "weatherDesc": [
        {
          "value": "Clear"
        }
      ],
      "weatherIconUrl": [
        {
          "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
        }
      ],
      "winddir16Point": "NNE",
      "winddirDegree": "25",
      "windspeedKmph": "4",
      "windspeedMiles": "2"
    }
  ],
  "nearest_area": [
    {
      "areaName": [
        {
          "value": "Berlin"
        }
      ],
      "country": [
        {
          "value": "Germany"
        }
      ],
      "latitude": "52.517",
      "longitude": "13.400",
      "population": "3426354",
      "region": [
        {
          "value": "Berlin"
        }
      ],
      "weatherUrl": [
        {
          "value": "https://www.worldweatheronline.com/v2/weather.aspx?q=52.517,13.4"
        }
      ]
    }
  ],
  "request": [
    {
      "query": "Lat 52.52 and Lon 13.41",
      "type": "LatLon"
    }
  ],
  "weather": [
    {
      "astronomy": [
        {
          "moon_illumination": "70",
          "moon_phase": "Waning Gibbous",
          "moonrise": "02:35 AM",
          "moonset": "08:49 AM",
          "sunrise": "06:25 AM",
          "sunset": "07:53 PM"
        }
      ],
      "avgtempC": "8",
      "avgtempF": "47",
      "date": "2026-04-08",
      "hourly": [
        {
          "DewPointC": "-3",
          "DewPointF": "27",
          "FeelsLikeC": "4",
          "FeelsLikeF": "40",
          "HeatIndexC": "6",
          "HeatIndexF": "42",
          "WindChillC": "4",
          "WindChillF": "40",
          "WindGustKmph": "11",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "82",
          "chanceofsnow": "0",
          "chanceofsunshine": "88",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "2",
          "diffRad": "0.0",
          "humidity": "55",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1029",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "6",
          "tempF": "42",
          "time": "0",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "NNE",
          "winddirDegree": "20",
          "windspeedKmph": "6",
          "windspeedMiles": "4"
        },
        {
          "DewPointC": "-3",
          "DewPointF": "26",
          "FeelsLikeC": "4",
          "FeelsLikeF": "38",
          "HeatIndexC": "4",
          "HeatIndexF": "40",
          "WindChillC": "4",
          "WindChillF": "38",
          "WindGustKmph": "8",
          "WindGustMiles": "5",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "90",
          "chanceofsnow": "0",
          "chanceofsunshine": "91",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "5",
          "diffRad": "0.0",
          "humidity": "57",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1030",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "4",
          "tempF": "40",
          "time": "300",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "NNE",
          "winddirDegree": "20",
          "windspeedKmph": "4",
          "windspeedMiles": "3"
        },
        {
          "DewPointC": "-4",
          "DewPointF": "25",
          "FeelsLikeC": "3",
          "FeelsLikeF": "38",
          "HeatIndexC": "3",
          "HeatIndexF": "38",
          "WindChillC": "3",
          "WindChillF": "38",
          "WindGustKmph": "6",
          "WindGustMiles": "3",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "81",
          "chanceofsnow": "0",
          "chanceofsunshine": "91",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "7",
          "diffRad": "0.0",
          "humidity": "58",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1030",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "3",
          "tempF": "38",
          "time": "600",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "NE",
          "winddirDegree": "42",
          "windspeedKmph": "3",
          "windspeedMiles": "2"
        },
        {
          "DewPointC": "-3",
          "DewPointF": "26",
          "FeelsLikeC": "6",
          "FeelsLikeF": "43",
          "HeatIndexC": "7",
          "HeatIndexF": "44",
          "WindChillC": "6",
          "WindChillF": "43",
          "WindGustKmph": "5",
          "WindGustMiles": "3",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "83",
          "chanceofsnow": "0",
          "chanceofsunshine": "88",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "15",
          "diffRad": "72.3",
          "humidity": "48",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1031",
          "pressureInches": "30",
          "shortRad": "263.5",
          "tempC": "7",
          "tempF": "44",
          "time": "900",
          "uvIndex": "1",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "NNE",
          "winddirDegree": "15",
          "windspeedKmph": "4",
          "windspeedMiles": "2"
        },
        {
          "DewPointC": "-3",
          "DewPointF": "27",
          "FeelsLikeC": "11",
          "FeelsLikeF": "51",
          "HeatIndexC": "11",
          "HeatIndexF": "52",
          "WindChillC": "11",
          "WindChillF": "51",
          "WindGustKmph": "8",
          "WindGustMiles": "5",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "92",
          "chanceofsnow": "0",
          "chanceofsunshine": "92",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "18",
          "diffRad": "73.3",
          "humidity": "38",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1030",
          "pressureInches": "30",
          "shortRad": "486.1",
          "tempC": "11",
          "tempF": "52",
          "time": "1200",
          "uvIndex": "3",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "NNE",
          "winddirDegree": "19",
          "windspeedKmph": "7",
          "windspeedMiles": "4"
        },
        {
          "DewPointC": "-2",
          "DewPointF": "28",
          "FeelsLikeC": "12",
          "FeelsLikeF": "54",
          "HeatIndexC": "13",
          "HeatIndexF": "56",
          "WindChillC": "12",
          "WindChillF": "54",
          "WindGustKmph": "12",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "86",
          "chanceofsnow": "0",
          "chanceofsunshine": "92",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "0",
          "diffRad": "81.7",
          "humidity": "34",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1029",
          "pressureInches": "30",
          "shortRad": "688.1",
          "tempC": "13",
          "tempF": "56",
          "time": "1500",
          "uvIndex": "3",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "NE",
          "winddirDegree": "45",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "-1",
          "DewPointF": "29",
          "FeelsLikeC": "11",
          "FeelsLikeF": "53",
          "HeatIndexC": "13",
          "HeatIndexF": "55",
          "WindChillC": "11",
          "WindChillF": "53",
          "WindGustKmph": "17",
          "WindGustMiles": "11",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "91",
          "chanceofsnow": "0",
          "chanceofsunshine": "89",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "3",
          "diffRad": "72.2",
          "humidity": "37",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1028",
          "pressureInches": "30",
          "shortRad": "520.7",
          "tempC": "13",
          "tempF": "55",
          "time": "1800",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "NE",
          "winddirDegree": "46",
          "windspeedKmph": "14",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "-0",
          "DewPointF": "31",
          "FeelsLikeC": "5",
          "FeelsLikeF": "41",
          "HeatIndexC": "8",
          "HeatIndexF": "46",
          "WindChillC": "5",
          "WindChillF": "41",
          "WindGustKmph": "24",
          "WindGustMiles": "15",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "89",
          "chanceofsnow": "0",
          "chanceofsunshine": "87",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "2",
          "diffRad": "0.0",
          "humidity": "56",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1029",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "8",
          "tempF": "46",
          "time": "2100",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "NE",
          "winddirDegree": "53",
          "windspeedKmph": "17",
          "windspeedMiles": "10"
        }
      ],
      "maxtempC": "13",
      "maxtempF": "56",
      "mintempC": "3",
      "mintempF": "38",
      "sunHour": "12.8",
      "totalSnow_cm": "0.0",
      "uvIndex": "1"
    },
    {
      "astronomy": [
        {
          "moon_illumination": "61",
          "moon_phase": "Waning Gibbous",
          "moonrise": "03:22 AM",
          "moonset": "09:48 AM",
          "sunrise": "06:22 AM",
          "sunset": "07:55 PM"
        }
      ],
      "avgtempC": "7",
      "avgtempF": "44",
      "date": "2026-04-09",
      "hourly": [
        {
          "DewPointC": "-0",
          "DewPointF": "32",
          "FeelsLikeC": "2",
          "FeelsLikeF": "36",
          "HeatIndexC": "5",
          "HeatIndexF": "41",
          "WindChillC": "2",
          "WindChillF": "36",
          "WindGustKmph": "20",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "88",
          "chanceofsnow": "0",
          "chanceofsunshine": "90",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "1",
          "diffRad": "0.0",
          "humidity": "69",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1029",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "5",
          "tempF": "41",
          "time": "0",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "64",
          "windspeedKmph": "13",
          "windspeedMiles": "8"
        },
        {
          "DewPointC": "-0",
          "DewPointF": "32",
          "FeelsLikeC": "1",
          "FeelsLikeF": "33",
          "HeatIndexC": "3",
          "HeatIndexF": "38",
          "WindChillC": "1",
          "WindChillF": "33",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "83",
          "chanceofsnow": "0",
          "chanceofsunshine": "94",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "21",
          "diffRad": "0.0",
          "humidity": "77",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1029",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "3",
          "tempF": "38",
          "time": "300",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "69",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "-2",
          "DewPointF": "28",
          "FeelsLikeC": "-1",
          "FeelsLikeF": "30",
          "HeatIndexC": "2",
          "HeatIndexF": "36",
          "WindChillC": "-1",
          "WindChillF": "30",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "10",
          "chanceofhightemp": "0",
          "chanceofovercast": "39",
          "chanceofrain": "0",
          "chanceofremdry": "91",
          "chanceofsnow": "0",
          "chanceofsunshine": "70",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "33",
          "diffRad": "0.0",
          "humidity": "73",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1029",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "2",
          "tempF": "36",
          "time": "600",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "116",
          "weatherDesc": [
            {
              "value": "Partly Cloudy "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "69",
          "windspeedKmph": "10",
          "windspeedMiles": "6"
        },
        {
          "DewPointC": "-4",
          "DewPointF": "24",
          "FeelsLikeC": "2",
          "FeelsLikeF": "35",
          "HeatIndexC": "4",
          "HeatIndexF": "40",
          "WindChillC": "2",
          "WindChillF": "35",
          "WindGustKmph": "14",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "83",
          "chanceofrain": "0",
          "chanceofremdry": "93",
          "chanceofsnow": "0",
          "chanceofsunshine": "13",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "99",
          "diffRad": "86.6",
          "humidity": "52",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1028",
          "pressureInches": "30",
          "shortRad": "255.8",
          "tempC": "4",
          "tempF": "40",
          "time": "900",
          "uvIndex": "1",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "73",
          "windspeedKmph": "12",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "-6",
          "DewPointF": "21",
          "FeelsLikeC": "7",
          "FeelsLikeF": "45",
          "HeatIndexC": "9",
          "HeatIndexF": "48",
          "WindChillC": "7",
          "WindChillF": "45",
          "WindGustKmph": "12",
          "WindGustMiles": "8",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "89",
          "chanceofsnow": "0",
          "chanceofsunshine": "87",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "0",
          "diffRad": "142.3",
          "humidity": "33",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1027",
          "pressureInches": "30",
          "shortRad": "448.9",
          "tempC": "9",
          "tempF": "48",
          "time": "1200",
          "uvIndex": "3",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "63",
          "windspeedKmph": "11",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "-7",
          "DewPointF": "19",
          "FeelsLikeC": "10",
          "FeelsLikeF": "50",
          "HeatIndexC": "12",
          "HeatIndexF": "53",
          "WindChillC": "10",
          "WindChillF": "50",
          "WindGustKmph": "15",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "94",
          "chanceofsnow": "0",
          "chanceofsunshine": "90",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "0",
          "diffRad": "75.8",
          "humidity": "26",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1025",
          "pressureInches": "30",
          "shortRad": "715.3",
          "tempC": "12",
          "tempF": "53",
          "time": "1500",
          "uvIndex": "3",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "60",
          "windspeedKmph": "13",
          "windspeedMiles": "8"
        },
        {
          "DewPointC": "-7",
          "DewPointF": "20",
          "FeelsLikeC": "9",
          "FeelsLikeF": "49",
          "HeatIndexC": "11",
          "HeatIndexF": "52",
          "WindChillC": "9",
          "WindChillF": "49",
          "WindGustKmph": "16",
          "WindGustMiles": "10",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "80",
          "chanceofsnow": "0",
          "chanceofsunshine": "91",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "0",
          "diffRad": "67.4",
          "humidity": "29",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1023",
          "pressureInches": "30",
          "shortRad": "543.0",
          "tempC": "11",
          "tempF": "52",
          "time": "1800",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "71",
          "windspeedKmph": "13",
          "windspeedMiles": "8"
        },
        {
          "DewPointC": "-6",
          "DewPointF": "22",
          "FeelsLikeC": "5",
          "FeelsLikeF": "41",
          "HeatIndexC": "7",
          "HeatIndexF": "45",
          "WindChillC": "5",
          "WindChillF": "41",
          "WindGustKmph": "19",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "93",
          "chanceofsnow": "0",
          "chanceofsunshine": "90",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "0",
          "diffRad": "0.0",
          "humidity": "40",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1023",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "7",
          "tempF": "45",
          "time": "2100",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "ENE",
          "winddirDegree": "79",
          "windspeedKmph": "11",
          "windspeedMiles": "7"
        }
      ],
      "maxtempC": "12",
      "maxtempF": "53",
      "mintempC": "2",
      "mintempF": "35",
      "sunHour": "12.5",
      "totalSnow_cm": "0.0",
      "uvIndex": "1"
    },
    {
      "astronomy": [
        {
          "moon_illumination": "52",
          "moon_phase": "Last Quarter",
          "moonrise": "03:57 AM",
          "moonset": "10:59 AM",
          "sunrise": "06:20 AM",
          "sunset": "07:56 PM"
        }
      ],
      "avgtempC": "5",
      "avgtempF": "42",
      "date": "2026-04-10",
      "hourly": [
        {
          "DewPointC": "-6",
          "DewPointF": "21",
          "FeelsLikeC": "2",
          "FeelsLikeF": "35",
          "HeatIndexC": "5",
          "HeatIndexF": "40",
          "WindChillC": "2",
          "WindChillF": "35",
          "WindGustKmph": "20",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "89",
          "chanceofsnow": "0",
          "chanceofsunshine": "88",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "0",
          "diffRad": "0.0",
          "humidity": "46",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1022",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "5",
          "tempF": "40",
          "time": "0",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Clear "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png"
            }
          ],
          "winddir16Point": "ESE",
          "winddirDegree": "106",
          "windspeedKmph": "12",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "-6",
          "DewPointF": "21",
          "FeelsLikeC": "-0",
          "FeelsLikeF": "31",
          "HeatIndexC": "3",
          "HeatIndexF": "38",
          "WindChillC": "-0",
          "WindChillF": "31",
          "WindGustKmph": "24",
          "WindGustMiles": "15",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "85",
          "chanceofrain": "0",
          "chanceofremdry": "88",
          "chanceofsnow": "0",
          "chanceofsunshine": "8",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "50",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1022",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "3",
          "tempF": "38",
          "time": "300",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "SE",
          "winddirDegree": "133",
          "windspeedKmph": "15",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "-6",
          "DewPointF": "22",
          "FeelsLikeC": "-1",
          "FeelsLikeF": "30",
          "HeatIndexC": "3",
          "HeatIndexF": "37",
          "WindChillC": "-1",
          "WindChillF": "30",
          "WindGustKmph": "25",
          "WindGustMiles": "16",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "84",
          "chanceofrain": "0",
          "chanceofremdry": "80",
          "chanceofsnow": "0",
          "chanceofsunshine": "17",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "54",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1020",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "3",
          "tempF": "37",
          "time": "600",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "SE",
          "winddirDegree": "131",
          "windspeedKmph": "16",
          "windspeedMiles": "10"
        },
        {
          "DewPointC": "-6",
          "DewPointF": "22",
          "FeelsLikeC": "1",
          "FeelsLikeF": "34",
          "HeatIndexC": "4",
          "HeatIndexF": "40",
          "WindChillC": "1",
          "WindChillF": "34",
          "WindGustKmph": "20",
          "WindGustMiles": "12",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "81",
          "chanceofrain": "66",
          "chanceofremdry": "0",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "50.9",
          "humidity": "47",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1020",
          "pressureInches": "30",
          "shortRad": "96.0",
          "tempC": "4",
          "tempF": "40",
          "time": "900",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "176",
          "weatherDesc": [
            {
              "value": "Patchy rain nearby"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0009_light_rain_showers.png"
            }
          ],
          "winddir16Point": "SE",
          "winddirDegree": "141",
          "windspeedKmph": "15",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "-4",
          "DewPointF": "25",
          "FeelsLikeC": "6",
          "FeelsLikeF": "43",
          "HeatIndexC": "8",
          "HeatIndexF": "47",
          "WindChillC": "6",
          "WindChillF": "43",
          "WindGustKmph": "17",
          "WindGustMiles": "11",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "0",
          "chanceofrain": "0",
          "chanceofremdry": "81",
          "chanceofsnow": "0",
          "chanceofsunshine": "93",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "17",
          "diffRad": "126.9",
          "humidity": "41",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "249.6",
          "tempC": "8",
          "tempF": "47",
          "time": "1200",
          "uvIndex": "1",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "113",
          "weatherDesc": [
            {
              "value": "Sunny"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
            }
          ],
          "winddir16Point": "SSE",
          "winddirDegree": "159",
          "windspeedKmph": "15",
          "windspeedMiles": "9"
        },
        {
          "DewPointC": "2",
          "DewPointF": "35",
          "FeelsLikeC": "6",
          "FeelsLikeF": "42",
          "HeatIndexC": "8",
          "HeatIndexF": "46",
          "WindChillC": "6",
          "WindChillF": "42",
          "WindGustKmph": "15",
          "WindGustMiles": "9",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "88",
          "chanceofrain": "100",
          "chanceofremdry": "0",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "32.0",
          "humidity": "67",
          "precipInches": "0.0",
          "precipMM": "0.2",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "47.4",
          "tempC": "8",
          "tempF": "46",
          "time": "1500",
          "uvIndex": "0",
          "visibility": "2",
          "visibilityMiles": "1",
          "weatherCode": "266",
          "weatherDesc": [
            {
              "value": "Light drizzle"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0017_cloudy_with_light_rain.png"
            }
          ],
          "winddir16Point": "W",
          "winddirDegree": "279",
          "windspeedKmph": "12",
          "windspeedMiles": "7"
        },
        {
          "DewPointC": "4",
          "DewPointF": "38",
          "FeelsLikeC": "5",
          "FeelsLikeF": "41",
          "HeatIndexC": "6",
          "HeatIndexF": "43",
          "WindChillC": "5",
          "WindChillF": "41",
          "WindGustKmph": "7",
          "WindGustMiles": "5",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "81",
          "chanceofrain": "70",
          "chanceofremdry": "0",
          "chanceofsnow": "0",
          "chanceofsunshine": "0",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "20.6",
          "humidity": "84",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "29.8",
          "tempC": "6",
          "tempF": "43",
          "time": "1800",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "176",
          "weatherDesc": [
            {
              "value": "Patchy rain nearby"
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0009_light_rain_showers.png"
            }
          ],
          "winddir16Point": "NW",
          "winddirDegree": "312",
          "windspeedKmph": "5",
          "windspeedMiles": "3"
        },
        {
          "DewPointC": "3",
          "DewPointF": "38",
          "FeelsLikeC": "4",
          "FeelsLikeF": "39",
          "HeatIndexC": "6",
          "HeatIndexF": "42",
          "WindChillC": "4",
          "WindChillF": "39",
          "WindGustKmph": "11",
          "WindGustMiles": "7",
          "chanceoffog": "0",
          "chanceoffrost": "0",
          "chanceofhightemp": "0",
          "chanceofovercast": "88",
          "chanceofrain": "0",
          "chanceofremdry": "90",
          "chanceofsnow": "0",
          "chanceofsunshine": "5",
          "chanceofthunder": "0",
          "chanceofwindy": "0",
          "cloudcover": "100",
          "diffRad": "0.0",
          "humidity": "84",
          "precipInches": "0.0",
          "precipMM": "0.0",
          "pressure": "1021",
          "pressureInches": "30",
          "shortRad": "0.0",
          "tempC": "6",
          "tempF": "42",
          "time": "2100",
          "uvIndex": "0",
          "visibility": "10",
          "visibilityMiles": "6",
          "weatherCode": "122",
          "weatherDesc": [
            {
              "value": "Overcast "
            }
          ],
          "weatherIconUrl": [
            {
              "value": "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
            }
          ],
          "winddir16Point": "N",
          "winddirDegree": "353",
          "windspeedKmph": "8",
          "windspeedMiles": "5"
        }
      ],
      "maxtempC": "10",
      "maxtempF": "50",
      "mintempC": "3",
      "mintempF": "37",
      "sunHour": "10.8",
      "totalSnow_cm": "0.0",
      "uvIndex": "0"
    }
  ]
}
```

```python
@mcp.tool()
def get_weather(city: str) -> str:
    """取得指定城市的即時天氣資訊。"""
    return get_weather_data(city)
```

### `tool_name`（負責：姓名）

- **功能**：
- **使用 API**：
- **參數**：
- **回傳範例**：

### `tool_name`（負責：姓名）

- **功能**：
- **使用 API**：
- **參數**：
- **回傳範例**：

---

## 心得

### 遇到最難的問題

> 寫下這次實作遇到最困難的事，以及怎麼解決的

### MCP 跟上週的 Tool Calling 有什麼不同？

> 用自己的話說說，做完後你覺得 MCP 的好處是什麼
