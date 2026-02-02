# ScaleDown — Recipe Compression & Lookup

Goal
- Compress a large recipe dataset (50k+ recipes) by ~80% while retaining fast and accurate retrieval for queries like "vegan dinner with chickpeas under 30 minutes".

Overview
1. Normalize recipes: canonicalize ingredient tokens, units, and steps.
2. Extract features: ingredient vectors, cuisine tags, cook time, dietary labels.
3. Dimensionality reduction: use PCA / autoencoder to create compact recipe embeddings.
4. Lossless metadata: keep minimal metadata (title, top ingredients, cook_time) for display.
5. Compression: quantize embeddings and store in a compact binary format.
6. Indexing: build small nearest-neighbor index (HNSW, annoy) over compressed embeddings.

Implementation Notes
- Preprocessing: unify units (g, tbsp, tsp), map synonyms (chickpeas → garbanzo beans).
- Use a tokenizer that keeps ingredients intact (multi-token phrases).
- Use an autoencoder architecture (small dense layers) to learn compact representations; an 80% size reduction target can be achieved by tuning latent dims and quantization.
- Optionally use product quantization (PQ) to shrink vectors further.

On-device Lookup
- Load quantized embeddings + small index in memory.
- For natural language queries, encode the query with the same encoder and run approximate nearest neighbor search.

Tradeoffs
- Higher compression increases false positives — tune recall/precision.
- Consider hybrid approach: compressed index for candidate retrieval, server-side full check for final ranking.

Deliverables
- `scripts/scaledown/` — ingestion, encoder training, quantization, and exporter scripts.
- Export format: `scaledb.bin` + `scaledb.meta.json` (schema + column mapping)
- Lookup API: lightweight `ScaledownLookup` class with `search(query_text, k=10)` method.
