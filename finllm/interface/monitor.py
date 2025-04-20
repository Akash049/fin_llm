
import argparse
import json
import time
from finllm.alerts.ticker_fetcher import fetch_ticker_data
from finllm.alerts.rule_engine import apply_rules
from finllm.alerts.telegram_alert import send_telegram_message
from finllm.alerts.parser import parse_alpha_vantage
from finllm.utils.env_loader import resolve_env_variables
from decouple import config


def run_monitor(llm_key, telegram_token, chat_id, ticker_config_path, rules_path):
    with open(ticker_config_path) as f:
        config_raw = f.read()
        config_raw = resolve_env_variables(config_raw)
        ticker_sources = json.loads(config_raw)["sources"]

    with open(rules_path) as f:
        rules = json.load(f)

    send_telegram_message(
        telegram_token,
        chat_id,
        f"🚀 FinLLM Monitor started for {len(ticker_sources)} source(s). Watching: " +
        ", ".join([src['name'] for src in ticker_sources])
    )

    while True:
        for source in ticker_sources:
            data_raw = fetch_ticker_data(source)
            data = parse_alpha_vantage(data_raw)
            if not data:
                continue
            print(f"✅ [Ticker Received] {source['name']}: {data}")
            alerts = apply_rules(data, rules, source["name"])
            for alert in alerts:
                send_telegram_message(telegram_token, chat_id, f"[ALERT] {source['name']}\n{alert}")
            time.sleep(source.get("poll_interval", 60))

def main():
    llm_key = config("LLM_KEY")
    telegram_bot_token = config("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = config("TELEGRAM_CHAT_ID")
    ticker_config = config("TICKER_CONFIG")
    rules_file = config("RULES_FILE")

    run_monitor(
        llm_key,
        telegram_bot_token,
        telegram_chat_id,
        ticker_config,
        rules_file
    )
