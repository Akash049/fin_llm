def parse_alpha_vantage(response_json):
    try:
        time_series = response_json.get("Time Series (1min)", {})
        if not time_series:
            raise ValueError("Missing 'Time Series (1min)' in response")

        # Extract latest price and volume
        sorted_times = sorted(time_series.keys(), reverse=True)
        latest_time = sorted_times[0]
        latest = time_series[latest_time]

        price = float(latest["1. open"])
        volume = int(float(latest["5. volume"]))

        # Extract closing prices for last 5 entries
        history = [float(time_series[ts]["4. close"]) for ts in sorted_times[:5]]

        return {
            "price": price,
            "volume": volume,
            "history": history
        }
    except Exception as e:
        print(f"[Parser Error]: {e}")
        return None
