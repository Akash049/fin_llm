
def safe_eval(expr, variables):
    try:
        return eval(expr, {"__builtins__": {}}, variables)
    except Exception as e:
        print(f"Rule evaluation error: {e}")
        return False

def apply_rules(data, rules, ticker_name):
    alerts = []
    for rule in rules:
        fields = {}
        for key, path in rule.get("fields", {}).items():
            try:
                fields[key] = eval(path, {"data": data})
            except Exception as e:
                print(f"Field eval failed: {e}")
        if safe_eval(rule["condition"], fields):
            msg = rule["message_template"].replace("{{ticker}}", ticker_name)
            alerts.append(msg)
    return alerts
