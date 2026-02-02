# Voice Command Specification

This document lists voice intents, example utterances, slots, and expected assistant behavior.

Core Intents

1. Recipe Search
- Examples: "Find a vegan chickpea curry", "Show me quick pasta recipes for two"
- Slots: `diet`, `main_ingredient`, `time_limit`, `servings`, `cuisine`
- Behavior: return top matches, read one-line summary, offer to open step-by-step.

2. Start Recipe / Step Navigation
- Examples: "Start recipe number 2", "Next step", "Repeat that", "Go back"
- Slots: `step_index`
- Behavior: read step audio, set timer if step includes timing, highlight card.

3. Timer Management
- Examples: "Set a 10-minute timer", "How much time is left on the oven timer?"
- Slots: `duration`, `timer_label`
- Behavior: create/track timers, speak updates, notify when finished.

4. Unit Conversion
- Examples: "Convert 200 grams to cups", "How many teaspoons in 2 tablespoons?"
- Slots: `quantity`, `from_unit`, `to_unit`
- Behavior: return conversion and optionally read it aloud.

5. Ingredient Substitution
- Examples: "What can I use instead of buttermilk?", "I don't have eggs — any substitutes?"
- Slots: `ingredient`
- Behavior: list 2-4 substitutions with tradeoffs.

6. Shopping List
- Examples: "Add eggs and milk to my shopping list", "Export shopping list"
- Slots: `items`
- Behavior: persist list, support export (CSV), and send via companion app.

7. Appliance Control
- Examples: "Preheat oven to 180°C", "Turn off the stove"
- Slots: `device`, `action`, `value`
- Behavior: send MQTT commands to the device and confirm success.

NLU / Parsing
- Use a small intent classifier + slot-filling CRF or a transformer-based parser for higher accuracy.
- Keep fallback prompts for ambiguous commands: "Did you mean X or Y?"

Voice UX
- Keep responses concise; confirm actions that are destructive (e.g., starting an appliance).
- Allow single-word confirmations: "Yes" / "No".
- Provide short auditory cues for step transitions (chime) and longer TTS for step instructions.
