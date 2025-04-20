# FinLLM – Real-Time Stock Intelligence & Alerting Assistant


**FinLLM** is an open-source Python package that connects to live stock ticker data, applies user-defined or built-in rules, and sends intelligent alerts to a Telegram bot. It optionally uses LLMs like OpenAI GPT or DeepSeek to generate meaningful financial commentary.

📘 [**Contribution Guide**](CONTRIBUTING.md) • 📜 [**Code of Conduct**](CODE_OF_CONDUCT.md)
---

## 🚀 What Can FinLLM Do?

- Connect to **multiple stock data sources**
- Define **custom or built-in rules** like price drops or volume spikes
- Use **LLM** (GPT/DeepSeek) to turn alerts into smart summaries
- Send **real-time alerts to Telegram**
- View and manage ticker sources via a **Streamlit UI**

---

## ⚙️ How It Works

1. Load multiple ticker URLs (e.g., AAPL, MSFT)
2. Periodically fetch price/volume data
3. Evaluate rules like:
   - "Price dropped 5% below 5-day moving average"
   - "Volume > 1.5× 7-day average"
4. Generate contextual alerts (optionally via LLM)
5. Send alert messages to Telegram channel or user

---

## 🧾 File Structure
```
fin-llm/ 
├── finllm/ 
│ ├── alerts/ # Ticker fetch, rules engine, Telegram alerts 
│ ├── interface/ # CLI runner for monitor 
│ ├── utils/ # Utility functions for data processing
├── config/ 
│ ├── ticker_config.json # Source APIs
│ └── rules_config.json # Rules for alerting 
├── streamlit_app/ # Streamlit UI to add/view tickers 
├── main.py # Starts Streamlit + Monitor 
├── Dockerfile 
└── requirements.txt
```


---

## ✅ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fin-llm.git
cd fin-llm
pip install -r requirements.txt
```

### 2. Configure Tickers and Rules
Edit `config/ticker_config.json` and `config/rules_config.json` to set up your ticker sources and alert rules.
```
{
  "sources": [
    {
      "name": "AAPL AlphaVantage",
      "url": "https://api.example.com/aapl",
      "headers": {
        "x-api-key": "your_api_key"
      },
      "poll_interval": 60
    }
  ]
}
```

```bash
## config/rules_config.json
[
  {
    "name": "Price Drop Alert",
    "condition": "current_price < moving_average_5 * 0.95",
    "fields": {
      "current_price": "data['price']",
      "moving_average_5": "sum(data['history'][-5:]) / 5"
    },
    "message_template": "⚠️ Price of {{ticker}} dropped >5% in 5-day window!"
  }
]
```

### 3. Set Up Telegram Bot
- Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather)
- Send a message to the bot and open the URL
- Look for "chat":{"id": ... } → this is your chat_id

### Run the Project
```bash
python main.py
```

### 4. Access the Streamlit UI
- Open your browser and go to `http://localhost:8501`
- Add or view tickers and rules
- Monitor alerts in real-time
- (Optional) Use LLM for generating summaries
- (Optional) Use Docker for deployment
- Build the Docker image
```bash
docker build -t finllm .
```
- Run the Docker container
```bash
docker run -p 8501:8501 finllm
```
- Access the Streamlit UI at `http://localhost:8501`
- (Optional) Use Docker Compose for multi-container setup

### ✨ Example Use Case
“Alert me on Telegram if AAPL's price drops 5% below its 5-day average or if volume exceeds 1.5× 7-day average.”

### 🤝 Contributing
* Fork the repo
* Add new ticker integrations, rules, or UI features
* Submit a PR with a description of your changes!

### 📜 License
MIT License — free to use, fork, and extend!

### Maintainer
Akash Chandra
Founder & CEO, InsightAI
Connect on LinkedIn



