import json
import re
from collections import Counter


def tokenize(s: str):
    return re.findall(r"\w+", s.lower())


class SimpleScaledown:
    """Very small, dependency-free recipe search prototype.

    Loads a JSON list of recipes with `title` and `ingredients` fields
    and scores by token overlap.
    """

    def __init__(self):
        self.recipes = []
        self.index = []

    def load(self, json_path: str):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                self.recipes = json.load(f)
        except Exception:
            self.recipes = []
        self.index = [Counter(tokenize((r.get("title","") + " " + " ".join(r.get("ingredients",[]))))) for r in self.recipes]

    def search(self, query: str, k: int = 5):
        qtok = Counter(tokenize(query))
        scores = []
        for i, idx in enumerate(self.index):
            # simple dot-product of token counts
            score = sum(min(qtok[t], idx.get(t, 0)) for t in qtok)
            if score > 0:
                scores.append((score, i))
        scores.sort(reverse=True)
        results = []
        for score, i in scores[:k]:
            r = self.recipes[i].copy()
            r.update({"score": score})
            results.append(r)
        return results
