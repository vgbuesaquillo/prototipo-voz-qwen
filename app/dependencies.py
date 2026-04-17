from fastapi import Request
from app.services.llm import QwenLLMService
from app.services.conversation import ConversationManager

async def get_llm_service(request: Request) -> QwenLLMService:
    return request.app.state.llm

async def get_conv_manager(request: Request) -> ConversationManager:
    return request.app.state.conversation
