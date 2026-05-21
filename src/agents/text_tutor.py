"""Text Tutor Agent — MiMo V2.5-Pro for Bahasa Indonesia explanations."""
from ..utils.mimo_client import MiMoClient

SYSTEM_PROMPT = """Kamu adalah tutor AI bernama Nusa yang mengajar siswa Indonesia.
- Jelaskan konsep dalam Bahasa Indonesia yang mudah dipahami
- Gunakan metode Socratic: ajukan pertanyaan untuk membimbing pemahaman
- Sesuaikan tingkat kesulitan dengan jenjang siswa (SD/SMP/SMA)
- Berikan contoh dari kehidupan sehari-hari di Indonesia"""


class TextTutorAgent:
    """Explains concepts in Bahasa Indonesia using Socratic questioning."""

    def __init__(self, client: MiMoClient):
        self.client = client
        self.name = "text_tutor"
        self.model = "mimo-v2.5-pro"

    async def explain(self, topic: str, grade_level: str, question: str) -> dict:
        prompt = (
            f"Topik: {topic}\n"
            f"Jenjang: {grade_level}\n"
            f"Pertanyaan siswa: {question}\n\n"
            f"Jelaskan konsepnya, lalu ajukan 1 pertanyaan pemantik."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)

    async def follow_up(self, context: str, student_answer: str) -> dict:
        prompt = (
            f"Konteks sebelumnya: {context}\n"
            f"Jawaban siswa: {student_answer}\n\n"
            f"Beri feedback positif, koreksi jika perlu, lalu lanjut ke konsep berikutnya."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)
