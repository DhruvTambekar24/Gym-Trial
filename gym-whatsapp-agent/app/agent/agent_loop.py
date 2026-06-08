from typing import Any

class AgentLoop:
    """Simple orchestration loop stub."""

    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools

    def run_once(self, prompt: str) -> Any:
        # Call LLM and possibly a tool
        return self.llm.generate(prompt)
