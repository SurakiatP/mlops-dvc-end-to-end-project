# 🚀 Model Deployment with GitHub Actions

This folder contains the setup for deploying the trained model using CI/CD via GitHub Actions.

## Files

- `serve_model.py`: Minimal Flask app to serve the model.
- `requirements.txt`: Dependencies for model serving.
- `deploy.yml`: GitHub Actions workflow to deploy the model on push/tag.

## How it works

1. On `git push` of a tag like `model-v1`, GitHub Actions runs the `deploy.yml` workflow.
2. It:
   - Installs dependencies
   - Restores model from DVC + GDrive remote
   - Starts model serving (can be modified to deploy on server)

## Usage

```bash
python serve_model.py
```
Then open: http://localhost:8000/predict
