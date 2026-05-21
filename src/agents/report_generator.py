"""Report Generator Agent — MiMo V2.5-Pro + TTS for parent/teacher reports."""
from ..utils.mimo_client import MiMoClient

SYSTEM_PROMPT = """Kamu adalah generator laporan pembelajaran AI.
- Buat laporan mingguan dalam Bahasa Indonesia untuk orang tua/guru
- Format: ringkas, mudah dipahami, dengan rekomendasi konkret
- Sertakan grafik progres (deskripsi) dan pencapaian
- Gunakan nada positif dan konstruktif"""


class ReportGeneratorAgent:
    """Weekly parent/teacher reports in Bahasa (text + audio)."""

    def __init__(self, client: MiMoClient):
        self.client = client
        self.name = "report_generator"
        self.models = ["mimo-v2.5-pro", "mimo-v2.5-tts"]

    async def generate_report(self, student_id: str, weekly_data: dict) -> dict:
        prompt = (
            f"Data mingguan siswa {student_id}: {weekly_data}\n\n"
            f"Buat laporan untuk orang tua dalam Bahasa Indonesia.\n"
            f"Format: Ringkasan, Pencapaian, Area Perbaikan, Rekomendasi."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)

    async def generate_audio_report(self, student_id: str, weekly_data: dict) -> dict:
        """Generate text report then convert to audio for parents."""
        report = await self.generate_report(student_id, weekly_data)
        audio = await self.client.synthesize(str(report))
        return {"report": report, "audio": audio}

    async def teacher_summary(self, class_id: str, all_students: list[dict]) -> dict:
        prompt = (
            f"Kelas: {class_id}\n"
            f"Data siswa: {all_students}\n\n"
            f"Buat ringkasan untuk guru: topik yang perlu diulang, siswa yang perlu perhatian."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)
