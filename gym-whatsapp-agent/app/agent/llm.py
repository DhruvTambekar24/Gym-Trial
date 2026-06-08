import json
from typing import Any

class LLM:
    """Minimal LLM wrapper stub."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def generate(self, prompt: str) -> dict:
        # Replace with actual API call (Groq/OpenAI/etc.)
        return {"response": f"Echo: {prompt}"}
