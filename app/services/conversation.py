import logging
from collections import deque
from app.config import Settings

logger = logging.getLogger(__name__)

class ConversationManager:
    def __init__(self, settings: Settings):
        self.history = deque(maxlen=settings.MAX_CONTEXT_TURNS * 2)

    def add_turn(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_context(self) -> list[dict]:
        return list(self.history)

    def clear(self):
        self.history.clear()
