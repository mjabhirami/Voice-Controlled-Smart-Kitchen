# Voice-Controlled Smart Kitchen

Hands-free cooking assistant that provides recipe search, step-by-step guidance with audio cues, timers, conversions, shopping lists, substitution suggestions, and IoT appliance control.

## Project Overview

Build a cooking assistant voice bot with hands-free control.

TECHNICAL SPECS: Integrate recipe APIs, implement voice commands for timers/conversions, use ScaleDown on recipe databases, create step-by-step guidance with audio cues, support IoT appliance control.

KEY FEATURES:
- Recipe search (natural language queries)
- Step-by-step instructions with voice and optional visual cards
- Ingredient substitution suggestions
- Timer management and conversion helpers
- Shopping list creation and export
- IoT appliance control (start/stop oven, set temperature, etc.)

SCALEDOWN BENEFITS:
- Compress 50,000+ recipes by ~80% for fast on-device lookups
- Instant recipe lookup for complex cooking queries
- Efficient memory/storage usage for embedded devices

DELIVERABLES:
- Kitchen voice assistant usable on PC/Raspberry Pi
- Recipe database with compressed lookup
- Cooking success rate measurement plan
- User experience study plan

## Contents
- `README.md` (this file)
- `docs/` — design and implementation documents

## Suggested Tech Stack
- Backend: Python (FastAPI) or Node.js (Express)
- Speech-to-text: OpenAI Whisper / Vosk / Google Speech-to-Text
- Text-to-speech: Coqui TTS / AWS Polly / Google TTS
- ScaleDown: custom compression pipeline (documented in `docs/ScaleDown.md`)
- Recipe API: Spoonacular / Edamam / TheMealDB
- Database: SQLite / PostgreSQL for server, local LRU cache for on-device
- IoT: MQTT (Mosquitto) + Home Assistant integration

## Quick start (developer)
1. Clone the repo:

```powershell
git clone https://github.com/mjabhirami/Voice-Controlled-Smart-Kitchen.git
cd "Voice-Controlled Smart Kitchen"
```

2. Create virtualenv and install dependencies (example Python):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Configure environment variables (API keys, MQTT broker):

- `RECIPE_API_KEY` — Spoonacular/Edamam key
- `MQTT_BROKER` — e.g., `mqtt://localhost:1883`
- `TTS_PROVIDER` / `STT_PROVIDER` keys

4. Run the voice assistant (local dev):

```powershell
# example command; adjust to your implementation
python -m app.main
```

## Contributing
- Follow the issues and project boards
- Open pull requests against `main`
- Add tests for new features (unit+integration)

## Next steps
- Complete `docs/` with architecture, ScaleDown details, voice command spec, and IoT integration.
- Implement creative feature and plan Build-in-Public posts.
