from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DEBUG: bool = False
    QWEN_API_KEY: str
    QWEN_BASE_URL: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    QWEN_MODEL: str = "qwen-turbo"
    MAX_CONTEXT_TURNS: int = 6

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
