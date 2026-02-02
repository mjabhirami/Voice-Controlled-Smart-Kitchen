# Creative / Unique Feature Proposal

Feature: Contextual Camera-Assisted Step Verification + Voice Hints

Summary
- Add an optional camera (phone/tablet/embedded) that verifies critical steps visually and gives voice hints.
- Example: When the step says "fold egg whites into batter until soft peaks form", the assistant can take a quick photo and either use a lightweight image classifier to confirm peaks or provide targeted guidance like "keep folding gently until you see soft peaks — about 10–15 folds".

Why it is unique
- Combines voice guidance with visual confirmation to reduce errors and increase cooking success rate.
- Useful for novice cooks and complex techniques.

Architecture
- Companion app or web UI captures occasional images (with user permission)
- Send downsampled frames to a small classifier running locally or on server
- Use lightweight models (MobileNet, tiny CNN) trained on labeled step images

Privacy
- Images processed only with explicit opt-in and can be processed locally to avoid uploading.

Implementation steps
1. Define step types that benefit from vision (whipping, searing, dough rise, browning).
2. Collect small dataset (mobile photos) and label examples.
3. Train tiny classifier and export as TFLite / ONNX.
4. Integrate into companion app; add voice prompts and fallback flow.

Deliverables
- `docs/creative_feature.md` (this file)
- A plan for dataset collection and a minimal prototype that runs inference on a phone
