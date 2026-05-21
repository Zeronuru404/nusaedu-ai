"""Progress Tracker Agent — MiMo V2.5-Pro for learning analytics."""
from ..utils.mimo_client import MiMoClient

SYSTEM_PROMPT = """Kamu adalah sistem tracking progres belajar AI.
- Analisis pola belajar siswa dari riwayat sesi
- Hitung skor penguasaan per topik (0-100)
- Sesuaikan tingkat kesulitan secara adaptif
- Deteksi siswa yang membutuhkan intervensi"""


class ProgressTrackerAgent:
    """Learning analytics, adaptive difficulty, mastery scoring."""

    def __init__(self, client: MiMoClient):
        self.client = client
        self.name = "progress_tracker"
        self.model = "mimo-v2.5-pro"

    async def update_progress(self, student_id: str, session_data: dict) -> dict:
        prompt = (
            f"ID Siswa: {student_id}\n"
            f"Data sesi: {session_data}\n\n"
            f"Update skor penguasaan dan rekomendasikan langkah selanjutnya."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)

    async def get_adaptive_difficulty(self, student_id: str, topic: str, current_mastery: float) -> dict:
        prompt = (
            f"Siswa: {student_id}\n"
            f"Topik: {topic}\n"
            f"Penguasaan saat ini: {current_mastery}%\n\n"
            f"Tentukan tingkat kesulitan berikutnya (mudah/sedang/sulit) dan alasan."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)

    async def flag_at_risk(self, student_id: str, history: list[dict]) -> dict:
        prompt = (
            f"Riwayat belajar siswa {student_id}: {history}\n\n"
            f"Apakah siswa ini perlu intervensi? Jelaskan indikatornya."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)
