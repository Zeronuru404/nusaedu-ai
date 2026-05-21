"""MiMo API client for multi-model inference."""
import httpx
from .config import Settings


class MiMoClient:
    """Unified client for MiMo V2.5 series models."""

    def __init__(self, settings: Settings | None = None):
        self.settings = settings or Settings()
        self._client = httpx.AsyncClient(
            base_url=self.settings.mimo_base_url,
            headers={"Authorization": f"Bearer {self.settings.mimo_api_key}"},
            timeout=60.0,
        )

    async def reason(self, prompt: str, system: str = "") -> dict:
        """MiMo V2.5-Pro: long-chain reasoning."""
        return await self._chat(self.settings.model_pro, prompt, system)

    async def analyze_image(self, prompt: str, image_url: str) -> dict:
        """MiMo V2.5-VL: vision-language analysis."""
        return await self._chat(
            self.settings.model_vl,
            prompt,
            extra={"image_url": image_url},
        )

    async def transcribe(self, audio_url: str) -> dict:
        """MiMo V2.5-ASR: speech-to-text."""
        return await self._chat(
            self.settings.model_asr,
            "Transcribe the following audio.",
            extra={"audio_url": audio_url},
        )

    async def synthesize(self, text: str) -> dict:
        """MiMo V2.5-TTS: text-to-speech."""
        return await self._chat(
            self.settings.model_tts,
            text,
        )

    async def _chat(self, model: str, prompt: str, system: str = "", extra: dict | None = None) -> dict:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        body = {"model": model, "messages": messages}
        if extra:
            body.update(extra)

        resp = await self._client.post("/chat/completions", json=body)
        resp.raise_for_status()
        return resp.json()

    async def close(self):
        await self._client.aclose()
