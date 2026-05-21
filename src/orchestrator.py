"""NusaEdu AI Orchestrator — coordinates all 6 agents."""
import asyncio
from .utils.mimo_client import MiMoClient
from .agents.text_tutor import TextTutorAgent
from .agents.vision_tutor import VisionTutorAgent
from .agents.voice_tutor import VoiceTutorAgent
from .agents.assessment import AssessmentAgent
from .agents.progress_tracker import ProgressTrackerAgent
from .agents.report_generator import ReportGeneratorAgent


class NusaEduOrchestrator:
    """Routes student queries to the right agent(s) and manages context."""

    def __init__(self, client: MiMoClient | None = None):
        self.client = client or MiMoClient()
        self.text_tutor = TextTutorAgent(self.client)
        self.vision_tutor = VisionTutorAgent(self.client)
        self.voice_tutor = VoiceTutorAgent(self.client)
        self.assessment = AssessmentAgent(self.client)
        self.progress = ProgressTrackerAgent(self.client)
        self.reports = ReportGeneratorAgent(self.client)

    async def handle_query(self, student_id: str, query: dict) -> dict:
        """Route a student query to the appropriate agent(s)."""
        query_type = query.get("type", "text")
        topic = query.get("topic", "umum")
        grade_level = query.get("grade_level", "SMP")

        if query_type == "text":
            result = await self.text_tutor.explain(topic, grade_level, query["question"])

        elif query_type == "image":
            result = await self.vision_tutor.analyze_image(
                query["image_url"], query.get("question", "Jelaskan gambar ini")
            )

        elif query_type == "voice":
            result = await self.voice_tutor.voice_explain(
                query["audio_url"], query.get("context", topic)
            )

        elif query_type == "quiz":
            result = await self.assessment.generate_quiz(topic, grade_level, query.get("num_questions", 5))

        elif query_type == "progress":
            result = await self.progress.update_progress(student_id, query.get("session_data", {}))

        elif query_type == "report":
            result = await self.reports.generate_report(student_id, query.get("weekly_data", {}))

        else:
            result = {"error": f"Unknown query type: {query_type}"}

        return {"student_id": student_id, "type": query_type, "result": result}

    async def learning_session(self, student_id: str, topic: str, grade_level: str) -> dict:
        """Full learning session: explain -> quiz -> feedback -> track progress."""
        # Step 1: Explain concept
        explanation = await self.text_tutor.explain(topic, grade_level, f"Jelaskan topik {topic}")

        # Step 2: Generate quiz
        quiz = await self.assessment.generate_quiz(topic, grade_level, 3)

        # Step 3: Update progress (stub - real impl would collect answers)
        progress = await self.progress.update_progress(student_id, {
            "topic": topic,
            "session_type": "learning",
            "completed": True,
        })

        return {
            "student_id": student_id,
            "topic": topic,
            "explanation": explanation,
            "quiz": quiz,
            "progress": progress,
        }

    async def close(self):
        await self.client.close()


async def main():
    """Example usage."""
    orchestrator = NusaEduOrchestrator()
    try:
        result = await orchestrator.handle_query("siswa-001", {
            "type": "text",
            "topic": "Fotosintesis",
            "grade_level": "SMP Kelas 7",
            "question": "Bagaimana proses fotosintesis pada tumbuhan?"
        })
        print(result)
    finally:
        await orchestrator.close()


if __name__ == "__main__":
    asyncio.run(main())
