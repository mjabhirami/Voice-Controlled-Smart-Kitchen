class VoiceEngine:
    """Simple stub for the voice engine.

    Replace or extend with real STT/TTS providers (Whisper/Google/Coqui/etc.).
    """

    def __init__(self, stt_provider=None, tts_provider=None):
        self.stt = stt_provider
        self.tts = tts_provider

    def listen(self):
        """Return transcribed text (placeholder)."""
        return ""

    def speak(self, text: str):
        """Speak text via TTS provider (placeholder)."""
        print("TTS:", text)
