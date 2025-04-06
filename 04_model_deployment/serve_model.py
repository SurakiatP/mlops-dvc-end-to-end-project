from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="Model Inference API",
    description="Serve trained ML model with FastAPI",
    version="1.0"
)

# Load the trained model
model = joblib.load("../models/model.pkl")

# --- Update this based on your actual features ---
# e.g., after featurize, you used TfidfVectorizer (300) + 3 numerical = 303 features
NUM_FEATURES = 303  # << Update accordingly if changed
# --------------------------------------------------

class InputData(BaseModel):
    data: list[list[float]]  # list of rows, each with 303 float features

@app.get("/")
def read_root():
    return {"message": "🚀 ML Model is ready to predict!"}

@app.post("/predict")
def predict(input: InputData):
    X = np.array(input.data)

    if X.ndim != 2 or X.shape[1] != NUM_FEATURES:
        raise HTTPException(
            status_code=400,
            detail=f"Each input row must have {NUM_FEATURES} features"
        )

    predictions = model.predict(X)
    return {"predictions": predictions.tolist()}

