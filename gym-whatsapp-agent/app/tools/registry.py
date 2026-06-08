from typing import Dict, Callable

registry: Dict[str, Callable] = {}

def register(name: str):
    def _inner(fn):
        registry[name] = fn
        return fn
    return _inner
