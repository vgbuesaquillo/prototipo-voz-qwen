import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.core.logging import setup_logging
from app.api.routes import router
from app.services.llm import QwenLLMService
from app.services.conversation import ConversationManager

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging(app.state.settings.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("🚀 Iniciando Qwen Voice Prototype...")
    app.state.llm = QwenLLMService(app.state.settings)
    app.state.conversation = ConversationManager(app.state.settings)
    yield
    logger.info("🛑 Aplicación cerrada")

app = FastAPI(title="Qwen Voice Prototype", version="1.0.0", lifespan=lifespan)
app.state.settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔒 Restringir en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
