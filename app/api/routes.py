from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.dependencies import get_llm_service, get_conv_manager
from app.services.llm import QwenLLMService
from app.services.conversation import ConversationManager

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"status": "ok", "version": "1.0.0"}

@router.post("/chat", response_model=ChatResponse)
async def chat(
    req: ChatRequest,
    llm: QwenLLMService = Depends(get_llm_service),
    conv: ConversationManager = Depends(get_conv_manager)
):
    try:
        context = conv.get_context()
        result = await llm.generate(context, req.text)
        conv.add_turn("user", req.text)
        conv.add_turn("assistant", result["reply"])
        return ChatResponse(reply=result["reply"], latency_ms=result["latency_ms"], turn_count=len(conv.history))
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno procesando la conversación")
