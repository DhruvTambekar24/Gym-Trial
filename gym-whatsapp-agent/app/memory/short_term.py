from collections import defaultdict
from typing import List

class ShortTermMemory:
    def __init__(self):
        self.store = defaultdict(list)  # phone -> list of messages

    def add_message(self, phone: str, message: str):
        self.store[phone].append(message)

    def get(self, phone: str) -> List[str]:
        return list(self.store[phone])
