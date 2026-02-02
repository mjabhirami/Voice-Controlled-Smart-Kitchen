# Testing Plan & UX Study

Testing Strategy
- Unit tests for parsing, conversions, timers, and IoT adapter logic
- Integration tests for recipe ingestion, ScaleDown lookup, and voice loop
- End-to-end tests using synthetic audio or text-driven harness

Metrics to measure
- Cooking success rate: user-reported success/failure per recipe
- Command accuracy: NLU intent+slot success rate
- Latency: STT→Action roundtrip time

User Study Outline
- Recruit 10–30 participants for a lab study and remote testing
- Tasks: search recipe, start recipe, handle substitutions, use timers, control device
- Collect SUS (System Usability Scale) and qualitative feedback

Data Collection
- Consent-driven voice logging for analysis
- Use anonymized telemetry: command counts, errors, latencies

Analysis
- Calculate success rate and error categories
- Identify friction points and update voice prompts or flows

Privacy
- Provide opt-in/out for data logging
- Delete voice logs upon user request
