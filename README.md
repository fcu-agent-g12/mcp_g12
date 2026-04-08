# MCP Server + AI agent 分組實作

> 課程：AI Agent 開發 — MCP（Model Context Protocol）
> 主題：每日生活顧問 (Daily Life Advisor)

---

## Server 功能總覽

這個 MCP Server 旨在成為使用者每天出門前的智慧助手，提供天氣資訊、靈感金句與健康建議。

| Tool 名稱      | 功能說明                                     | 負責組員 |
| -- | -- | -- |
| -- | -- | -- |
| `get_advice`    | 獲取今日金句或生活建議 (使用 Advice Slip) | 何平 |
| -- | -- | -- |
| -- | -- | -- |

---

## 組員與分工

| 姓名   | 負責功能            | 檔案                   | 使用的 API         |
| -- | -- | -- | -- |
| -- | -- | -- | -- |
| 何平 | 獲取今日金句或生活建議 | `get_advice` | https://api.adviceslip.com/advice ｜
| -- | -- | -- | -- |
| -- | -- | -- | -- |

---

## 專案架構

```
├── server.py              # MCP Server 主程式
├── agent.py               # MCP Client + Gemini Agent（用 AI 產生）
├── tools/
│   ├── __init__.py
│   ├── weather_tool.py    # 天氣查詢工具
│   ├── quote_tool.py      # 今日金句工具
│   └── example_tool.py    # 範例
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 使用方式

```bash
# 1. 建立虛擬環境
python3 -m venv venv
source venv/bin/activate

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 設定 API Key
# 編輯 .env，填入你的 GEMINI_API_KEY

# 4. 啟動 Server
python server.py

# 5. 啟動 MCP Inspector 測試
npx @modelcontextprotocol/inspector http://localhost:8000/sse

# 6. 用 Agent 對話
python agent.py
```

---

## 測試結果

### MCP Inspector 截圖
- **Tools**: 已確認 `get_weather` 和 `get_quote` 可用。
- **Resources**: 已確認 `info://healthy-habits` 可讀取。
- **Prompts**: 已確認 `plan_my_day` 可填入城市參數。

### Agent 對話截圖
- Agent 成功調用工具鏈：先呼叫 `get_quote` 提供金句，再呼叫 `get_weather` 提供天氣資訊，最後整合為完整回覆。

---

## 各 Tool 說明

### `get_weather`
- **功能**：獲取即時天氣。
- **使用 API**：`wttr.in`
- **參數**：`city` (str)
- **回傳範例**：`台北 目前天气：Light rain，温度：22°C...`

### `get_quote`
- **功能**：獲取每日金句。
- **使用 API**：`api.adviceslip.com`
- **參數**：無
- **回傳範例**：`今日給您的小建議：試著「Measure twice, cut once.」...`

---

## 心得

### 遇到最難的問題
在啟動 MCP Inspector 時遇到了端口占用（6277, 6274）的問題，通過 `lsof` 查找進程並強行清理後成功啟動。此外，Gemini 模型版本的名稱匹配也經過了幾次調試。

### MCP 跟上週的 Tool Calling 有什麼不同？
MCP 將工具（Tools）、資源（Resources）與提示詞（Prompts）標準化，使得不同的 Client 都能以統一的協議與 Server 溝通，這大大提升了工具的可重用性與 Agent 的開發效率。
