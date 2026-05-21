# 🎓 NusaEdu AI

**Multi-Modal AI Tutor for Indonesian Schools** — powered by Xiaomi MiMo V2.5

> 6 AI agents using Pro (reasoning), VL (vision), ASR (speech), TTS (voice) to deliver personalized education for 270M Indonesians.

## Architecture

```
                    ┌─────────────────────────┐
                    │      Orchestrator       │
                    │   (MiMo V2.5-Pro)       │
                    │   Route + Context Mgr   │
                    └──────────┬──────────────┘
                               │
          ┌──────────┬─────────┼─────────┬──────────┐
          ▼          ▼         ▼         ▼          ▼
   ┌──────────┐ ┌─────────┐ ┌──────┐ ┌────────┐ ┌──────────┐
   │  Text    │ │ Vision  │ │Voice │ │Assess- │ │ Progress │
   │  Tutor   │ │ Tutor   │ │Tutor │ │  ment  │ │ Tracker  │
   │ V2.5-Pro │ │V2.5-VL  │ │ASR+  │ │V2.5-Pro│ │V2.5-Pro  │
   │          │ │         │ │TTS   │ │        │ │          │
   └──────────┘ └─────────┘ └──────┘ └────────┘ └──────────┘
                                                      │
                                               ┌──────┴──────┐
                                               │   Report    │
                                               │  Generator  │
                                               │  V2.5-Pro   │
                                               │  + TTS      │
                                               └─────────────┘
```

## Agents

| Agent | Model | Role | Tokens/Run |
|---|---|---|---|
| **Orchestrator** | MiMo V2.5-Pro | Routes queries, manages context, coordinates agents | ~2,500 |
| **Text Tutor** | MiMo V2.5-Pro | Explains concepts in Bahasa Indonesia, Socratic Q&A | ~8,000 |
| **Vision Tutor** | MiMo V2.5-VL | Analyzes diagrams, textbook pages, handwritten math | ~4,000 |
| **Voice Tutor** | ASR + TTS | Speech-to-text input, spoken explanations output | ~3,000 |
| **Assessment** | MiMo V2.5-Pro | Generates quizzes, grades answers, identifies gaps | ~6,000 |
| **Progress Tracker** | MiMo V2.5-Pro | Learning analytics, adaptive difficulty, mastery scoring | ~3,000 |
| **Report Generator** | V2.5-Pro + TTS | Weekly parent/teacher reports in Bahasa (text + audio) | ~5,000 |

**Total per student session:** ~31,500 tokens

## Token Consumption Model

```
Per student:
  3 sessions/day × 31,500 tokens = 94,500 tokens/day

At 50,000 students (Year 1 target):
  50,000 × 94,500 = 4.725B tokens/day
  Monthly: ~141.75B tokens/month

At 200,000 students (Year 2 target):
  200,000 × 94,500 = 18.9B tokens/day
  Monthly: ~567B tokens/month
```

| Scale | Students | Tokens/Day | Tokens/Month |
|---|---|---|---|
| Pilot | 1,000 | 94.5M | 2.8B |
| Year 1 | 50,000 | 4.7B | 141.8B |
| Year 2 | 200,000 | 18.9B | 567B |

## Why Indonesian Education?

- **270M population**, 45M+ students in K-12
- **Teacher shortage**: 1.2M teachers short (Kemendikbud 2025)
- **Digital gap**: 73% students have smartphones but <15% use AI learning tools
- **Language barrier**: Existing AI tutors are English-first, miss Bahasa nuance
- **Government push**: Kurikulum Merdeka mandates personalized learning

## Tech Stack

- **Framework**: Python 3.11 + asyncio
- **Models**: MiMo V2.5-Pro, V2.5-VL, V2.5-ASR, V2.5-TTS
- **Agent Orchestration**: Custom multi-agent pipeline
- **Tools**: Hermes Agent, Cursor, Claude Code
- **API**: Xiaomi MiMo Open Platform (platform.xiaomimimo.com)

## Target Users

- Indonesian K-12 students (SD, SMP, SMA)
- Teachers needing AI-assisted grading and reporting
- Parents wanting progress visibility
- Schools seeking affordable AI tutoring at scale

## Status

🚧 Development in progress — seeking MiMo API credits for production scale.

## License

MIT
