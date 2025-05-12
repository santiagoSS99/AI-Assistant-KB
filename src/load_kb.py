import json

def load_kb(path="data/knowledge_base.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)