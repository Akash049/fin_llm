import streamlit as st

st.set_page_config(page_title="📘 FinLLM Rule Guide", layout="centered")
st.title("📘 FinLLM Rule Configuration Guide")

st.markdown("""
### What is a Rule?

A rule in FinLLM tells the system **when to send an alert** based on live stock data.

---

### 🛠 Rule Format (JSON)

```json
{
  "name": "Volume Spike",
  "condition": "volume > avg_volume * 1.5",
  "fields": {
    "volume": "data['volume']",
    "avg_volume": "sum(data['history']) / len(data['history'])"
  },
  "message_template": "🚨 Volume spike for {{ticker}}!"
}
```

---

### 🔍 Field Descriptions

- `name`: A friendly name for the rule.
- `condition`: A Python expression that evaluates to `True` or `False`.
- `fields`: Dynamic values calculated from live ticker data.
- `message_template`: Message sent to Telegram. You can use `{{ticker}}`.

---

### ✅ Example (Price Check)

```json
{
  "name": "Price Check",
  "condition": "current_price > 100",
  "fields": {
    "current_price": "data['price']"
  },
  "message_template": "📈 Price is above $100!"
}
```

---

### ✍️ How to Add Rules

1. Open `config/rules_config.json`
2. Add your rule(s) following the above structure
3. Restart `main.py` or the Docker container
4. New rules will be applied in the next poll cycle

Happy monitoring! 🚀
""")