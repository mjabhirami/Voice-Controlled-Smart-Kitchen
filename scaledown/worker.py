class ScaledownWorker:
    """Stub for scaledown training, quantization and lookup."""

    def __init__(self, model_path: str = None):
        self.model_path = model_path

    def train(self, recipes):
        print("Training scaledown encoder (stub)")

    def export(self, out_path: str = "scaledb.bin"):
        print(f"Exporting scaledown DB to {out_path} (stub)")

    def search(self, query: str, k: int = 10):
        return []
