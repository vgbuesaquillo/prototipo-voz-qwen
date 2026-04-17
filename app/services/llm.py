import time
import logging
from openai import AsyncOpenAI
from app.config import Settings

logger = logging.getLogger(__name__)

class QwenLLMService:
    def __init__(self, settings: Settings):
        self.client = AsyncOpenAI(api_key=settings.QWEN_API_KEY, base_url=settings.QWEN_BASE_URL)
        self.model = settings.QWEN_MODEL
        self.system_prompt = "Eres un asistente de voz profesional, conciso y natural. Responde en español. Evita markdown y listas largas."

    async def generate(self, history: list[dict], user_input: str) -> dict:
        messages = [{"role": "system", "content": self.system_prompt}] + history + [{"role": "user", "content": user_input}]
        start = time.perf_counter()
        try:
            res = await self.client.chat.completions.create(model=self.model, messages=messages, max_tokens=120, temperature=0.7)
            reply = res.choices[0].message.content.strip()
            latency = (time.perf_counter() - start) * 1000
            logger.info(f"✅ LLM response in {latency:.0f}ms")
            return {"reply": reply, "latency_ms": latency}
        except Exception as e:
            logger.error(f"❌ LLM error: {str(e)}")
            raise
