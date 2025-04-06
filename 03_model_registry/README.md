# 📚 03_model_registry

This folder serves as a lightweight **Model Registry** for tracking and managing model versions trained throughout the project lifecycle.

## 📦 Purpose

In a typical MLOps workflow, model registry is essential for:

- Tracking model versions (v1, v2, ...)
- Storing performance metrics (accuracy, f1, recall, etc.)
- Logging experiment configurations (hyperparameters, feature sets)
- Tagging production-ready models via Git + DVC

## 📁 Files

- `registry_info.md`: Manual changelog of model versions, metrics, parameters, and related tags.
- `README.md`: This documentation file.

## 🔖 Versioning Strategy

We use a simple Git-based versioning strategy with DVC:

1. **Train model** via `dvc exp run`
2. **Select best model** based on metrics
3. Commit `dvc.lock` and tag with `git tag -a model-vX -m "..."`  
4. Log the details in `registry_info.md`

## 🚀 Example Git Commands

```bash
git add 01_data_pipelines/dvc.lock models/.gitignore
git commit -m "Register model-v2 from experiment"
git tag -a model-v2 -m "Trained with max_iter=2000"
```
## ✅ Benefits
- Simple, Git-based, no external tools
- Transparent and auditable history
- Easy to automate in CI/CD (step: deploy only tagged models)