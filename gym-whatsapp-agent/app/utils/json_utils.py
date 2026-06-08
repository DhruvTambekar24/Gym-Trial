import json

def parse_json_safe(s: str):
    try:
        return json.loads(s)
    except Exception:
        return None
