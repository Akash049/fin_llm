
import requests

def fetch_ticker_data(source):
    try:
        response = requests.get(source["url"], headers=source.get("headers", {}))
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {source['name']}: {e}")
        return None
