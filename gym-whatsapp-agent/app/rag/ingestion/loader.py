from pathlib import Path

def load_corpus(path: str):
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")
