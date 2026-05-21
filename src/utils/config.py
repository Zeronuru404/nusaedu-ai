"""Configuration via environment variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mimo_api_key: str = ""
    mimo_base_url: str = "https://api.xiaomimimo.com/v1"

    # Model routing
    model_pro: str = "mimo-v2.5-pro"
    model_vl: str = "mimo-v2.5-vl"
    model_asr: str = "mimo-v2.5-asr"
    model_tts: str = "mimo-v2.5-tts"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
