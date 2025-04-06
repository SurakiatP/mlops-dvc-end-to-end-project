# 📘 Model Version Registry

This document records details of all model versions trained and registered in this project.

---

## 📦 model-v1

- 🏷 **Git Tag**: `model-v1`
- 📅 **Date**: 2025-04-05
- 🧪 **Experiment**: `dvc exp run` (Logistic Regression)
- ⚙️ **Parameters**:
  - `model_type`: LogisticRegression
  - `max_iter`: 1500
  - `threshold`: 0.5
- 📈 **Metrics**:
  - `accuracy`: 0.8132
  - `precision`: 0.8711
  - `recall`: 0.8302
  - `f1_score`: 0.8501
- 📁 **Model Path**: `models/model.pkl`
- 📂 **Lock File**: `01_data_pipelines/dvc.lock`
- 📌 **Notes**:
  - Binary classification (`Score >= 5`)
  - Feature set: `Title + Tags + Body + ViewCount + AnswerCount + CommentCount`
  - Model not yet deployed

---

## 📘 How to Add New Versions

1. Run new experiments using `dvc exp run`
2. Choose the best performing experiment
3. Commit lockfile and tag:
   ```bash
   git add 01_data_pipelines/dvc.lock models/.gitignore
   git commit -m "Register model-vX from experiment"
   git tag -a model-vX -m "..."
---
## ✍️ Keep this file updated for clear traceability and reproducibility.

- Whenever you create `model-v2` or a later version, simply copy the block above and edit the details to match that version!

