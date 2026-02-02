# Architecture Overview

This document describes the high-level architecture for the Voice-Controlled Smart Kitchen.

Components
- Voice Engine (STT + Command Parser)
  - Capture audio from microphone
  - Run speech-to-text (Whisper / Vosk / Google STT)
  - Parse intent and entities (NLU module)

- Dialogue Manager / Orchestrator
  - Maintain session state (current recipe, step index)
  - Handle timers, conversions, confirmations
  - Emit TTS cues and visual cards

- Recipe Database + ScaleDown Layer
  - Raw ingestion from recipe APIs (Spoonacular, Edamam)
  - Preprocessing and normalization
  - ScaleDown compression for on-device lookup
  - Fast search index (annoy/FAISS or in-memory lookup)

- Backend API
  - Exposes endpoints for search, recipe retrieval, and user data
  - Auth + user preferences

- IoT Integration Layer
  - MQTT client and device adapters
  - Device discovery & capability negotiation
  - Secure command channel for appliance control

- UI / Companion App (optional)
  - Visual recipe cards, step highlighting, and shopping list export

Communication
- Voice client ↔ Backend: WebSocket or GRPC for low-latency session updates
- Backend ↔ IoT Devices: MQTT (recommended) or direct cloud APIs
- Local-only mode: everything runs on-device using local model instances

Resilience
- Offline fallback: cached recipes + local TTS/STT models
- Retry policies for external APIs and MQTT connectivity

Security & Privacy
- Store PII and voice logs encrypted at rest
- Allow opt-out for server-side logging of voice data
- Rate-limit external API calls and cache results
