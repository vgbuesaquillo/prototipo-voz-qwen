from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)

class ChatResponse(BaseModel):
    reply: str
    latency_ms: float | None = None
    turn_count: int
