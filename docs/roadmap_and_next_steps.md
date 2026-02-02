# Roadmap & Next Steps

Phase 0 — Docs & Design (current)
- Finalize README and docs
- Choose tech stack and initial APIs

Phase 1 — Core Prototype
- Implement voice loop (STT -> intent -> action -> TTS)
- Recipe ingestion pipeline and scaledown exporter
- Timer and conversions module

Phase 2 — IoT & Companion App
- MQTT device adapters and Home Assistant integration
- Companion app for visual cards and shopping list export

Phase 3 — Creative Feature & UX Study
- Build camera-assisted verification prototype
- Run initial UX study and measure cooking success rate

Phase 4 — Polish & Build-in-Public
- Improve NLU accuracy, reduce latency
- Publish progress posts and release a demo

Priority tasks to start coding
- `voice/` module scaffold (STT/TTS abstraction)
- `recipes/` ingestion + `scaledown/` scripts
- `timers/` module with persistence
- `iot/` MQTT adapter and mock devices

Notes
- Keep the system modular so features can be swapped (different STT/TTS or ScaleDown variants)
