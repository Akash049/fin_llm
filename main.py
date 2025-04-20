import threading
import subprocess
from finllm.interface.monitor import run_monitor
from decouple import config

def start_monitor():
    run_monitor(
        llm_key=config("LLM_KEY"),
        telegram_token=config("TELEGRAM_BOT_TOKEN"),
        chat_id=config("TELEGRAM_CHAT_ID"),
        ticker_config_path=config("TICKER_CONFIG"),
        rules_path=config("RULES_FILE")
    )

def start_streamlit_main():
    subprocess.run(["streamlit", "run", "streamlit_app/dashboard.py", "--server.port=8501"])

def start_streamlit_guide():
    subprocess.run(["streamlit", "run", "streamlit_app/rule_guide.py", "--server.port=8502"])


if __name__ == "__main__":
    threading.Thread(target=start_streamlit_main).start()
    threading.Thread(target=start_streamlit_guide).start()
    start_monitor()
