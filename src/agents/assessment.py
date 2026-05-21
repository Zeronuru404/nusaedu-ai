"""Assessment Agent — MiMo V2.5-Pro for quiz generation and grading."""
from ..utils.mimo_client import MiMoClient

SYSTEM_PROMPT = """Kamu adalah asisten penilaian AI untuk sekolah Indonesia.
- Buat soal sesuai jenjang (SD/SMP/SMA) dan topik
- Format: pilihan ganda (4 opsi), isian singkat, atau esai singkat
- Beri penilaian objektif dengan feedback konstruktif
- Identifikasi area yang perlu diperbaiki siswa"""


class AssessmentAgent:
    """Generates quizzes, grades answers, identifies knowledge gaps."""

    def __init__(self, client: MiMoClient):
        self.client = client
        self.name = "assessment"
        self.model = "mimo-v2.5-pro"

    async def generate_quiz(self, topic: str, grade_level: str, num_questions: int = 5) -> dict:
        prompt = (
            f"Topik: {topic}\n"
            f"Jenjang: {grade_level}\n"
            f"Jumlah soal: {num_questions}\n\n"
            f"Buat soal pilihan ganda dengan 4 opsi dan kunci jawaban."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)

    async def grade_answer(self, question: str, student_answer: str, correct_answer: str) -> dict:
        prompt = (
            f"Soal: {question}\n"
            f"Jawaban siswa: {student_answer}\n"
            f"Jawaban benar: {correct_answer}\n\n"
            f"Beri penilaian (benar/salah/sebagian) dan feedback."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)

    async def identify_gaps(self, quiz_results: list[dict]) -> dict:
        prompt = (
            f"Hasil kuis siswa:\n{quiz_results}\n\n"
            f"Identifikasi topik yang belum dikuasai dan rekomendasikan materi review."
        )
        return await self.client.reason(prompt, system=SYSTEM_PROMPT)
