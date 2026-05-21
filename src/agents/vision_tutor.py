"""Vision Tutor Agent — MiMo V2.5-VL for image analysis."""
from ..utils.mimo_client import MiMoClient

SYSTEM_PROMPT = """Kamu adalah tutor visual AI. Analisis gambar yang dikirim siswa:
- Identifikasi konten (diagram, teks buku, soal matematika, dll)
- Jelaskan apa yang terlihat dalam Bahasa Indonesia
- Bantu siswa memahami visual tersebut langkah demi langkah"""


class VisionTutorAgent:
    """Analyzes diagrams, textbook pages, and handwritten math."""

    def __init__(self, client: MiMoClient):
        self.client = client
        self.name = "vision_tutor"
        self.model = "mimo-v2.5-vl"

    async def analyze_image(self, image_url: str, question: str) -> dict:
        prompt = (
            f"Siswa mengirim gambar dengan pertanyaan: {question}\n\n"
            f"Analisis gambar ini dan jelaskan dalam Bahasa Indonesia."
        )
        return await self.client.analyze_image(prompt, image_url)

    async def solve_math(self, image_url: str) -> dict:
        prompt = (
            "Siswa mengirim foto soal matematika.\n"
            "1. Identifikasi soal dari gambar\n"
            "2. Selesaikan langkah demi langkah\n"
            "3. Jelaskan setiap langkah dalam Bahasa Indonesia"
        )
        return await self.client.analyze_image(prompt, image_url)
