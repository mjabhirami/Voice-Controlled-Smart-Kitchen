import math
import json
import re
from collections import Counter, defaultdict


def tokenize(text: str):
    return re.findall(r"\w+", text.lower())


class TFIDFSearch:
    """Tiny TF-IDF search implementation without external deps.

    Expects a JSON file: list of recipes with `title` and `ingredients`.
    """

    def __init__(self):
        self.docs = []
        self.doc_freq = defaultdict(int)
        self.doc_tokens = []
        self.N = 0

    def load(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.docs = json.load(f)
        except Exception:
            self.docs = []
        self.N = len(self.docs)
        self.doc_tokens = []
        self.doc_freq = defaultdict(int)
        for doc in self.docs:
            text = doc.get("title", "") + " " + " ".join(doc.get("ingredients", []))
            toks = tokenize(text)
            uniq = set(toks)
            for t in uniq:
                self.doc_freq[t] += 1
            self.doc_tokens.append(Counter(toks))

    def _idf(self, term: str):
        df = self.doc_freq.get(term, 0)
        if df == 0:
            return 0.0
        return math.log(self.N / df)

    def _tfidf(self, q_counter: Counter, doc_counter: Counter):
        score = 0.0
        for term, qcount in q_counter.items():
            if qcount <= 0:
                continue
            tf = doc_counter.get(term, 0)
            if tf == 0:
                continue
            score += (qcount * self._idf(term) * tf)
        return score

    def search(self, query: str, k: int = 5):
        qtok = Counter(tokenize(query))
        scores = []
        for i, doc_counter in enumerate(self.doc_tokens):
            s = self._tfidf(qtok, doc_counter)
            if s > 0:
                scores.append((s, i))
        scores.sort(reverse=True)
        results = []
        for score, i in scores[:k]:
            r = self.docs[i].copy()
            r.update({"score": score})
            results.append(r)
        return results
