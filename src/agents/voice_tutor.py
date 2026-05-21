"""Voice Tutor Agent — MiMo V2.5-ASR + TTS for speech interaction."""
from ..utils.mimo_client import MiMoClient


class VoiceTutorAgent:
    """Speech-to-text input and spoken explanations output."""

    def __init__(self, client: MiMoClient):
        self.client = client
        self.name = "voice_tutor"
        self.models = ["mimo-v2.5-asr", "mimo-v2.5-tts"]

    async def listen(self, audio_url: str) -> dict:
        """Convert student speech to text."""
        return await self.client.transcribe(audio_url)

    async def speak(self, explanation: str) -> dict:
        """Convert text explanation to speech."""
        return await self.client.synthesize(explanation)

    async def voice_explain(self, audio_url: str, context: str) -> dict:
        """Full voice loop: listen -> reason -> speak."""
        # Step 1: Transcribe student question
        transcript = await self.listen(audio_url)

        # Step 2: Generate explanation
        explanation = await self.client.reason(
            f"Pertanyaan siswa (dari suara): {transcript}\nKonteks: {context}",
            system="Jelaskan dalam Bahasa Indonesia yang natural dan cocok untuk diucapkan."
        )

        # Step 3: Convert to speech
        audio = await self.speak(str(explanation))

        return {"transcript": transcript, "explanation": explanation, "audio": audio}
