from dataclasses import dataclass

@dataclass
class AgentState:
    iterations: int = 0
    last_response: str = ""

    def tick(self):
        self.iterations += 1
