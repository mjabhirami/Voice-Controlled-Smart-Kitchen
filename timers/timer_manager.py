import threading
import time


class TimerManager:
    def __init__(self):
        self.timers = {}

    def set_timer(self, label: str, seconds: int):
        def _run():
            time.sleep(seconds)
            print(f"Timer '{label}' finished")

        t = threading.Thread(target=_run, daemon=True)
        t.start()
        self.timers[label] = {"seconds": seconds, "thread": t}
        return True

    def list_timers(self):
        return {k: v["seconds"] for k, v in self.timers.items()}
