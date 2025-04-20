import streamlit as st
import json

st.set_page_config(page_title="FinLLM Ticker Monitor", layout="wide")

st.title("📊 FinLLM - Stock Ticker Monitor")

with st.sidebar:
    st.header("Add New Ticker Source")
    st.markdown("[📘 Open Rule Guide](http://localhost:8502)", unsafe_allow_html=True)
    name = st.text_input("Source Name")
    url = st.text_input("API URL")
    api_key = st.text_input("API Key (optional)")
    interval = st.number_input("Poll Interval (seconds)", min_value=10, step=10)

    if st.button("Add Ticker"):
        try:
            with open("config/ticker_config.json", "r+") as f:
                config = json.load(f)
                config["sources"].append({
                    "name": name,
                    "url": url,
                    "headers": {"x-api-key": api_key} if api_key else {},
                    "poll_interval": interval
                })
                f.seek(0)
                json.dump(config, f, indent=2)
                f.truncate()
            st.success("Ticker added!")
        except Exception as e:
            st.error(f"Error: {e}")

st.header("Current Ticker Config")

try:
    with open("config/ticker_config.json", "r") as f:
        config = json.load(f)
        st.json(config)
except Exception as e:
    st.warning("Could not load ticker config.")
