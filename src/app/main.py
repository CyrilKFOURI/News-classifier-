import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import sys
from pathlib import Path
import uvicorn

# Allow importing from src
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

app = FastAPI(
    title="Music Recommender API",
    description="API to recommend music categories based on text input (currently using BBC News model as placeholder)",
    version="1.0.0"
)

# Global variable to hold the model
model = None

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    category: str
    confidence: float = 0.0 # Placeholder for confidence if available

@app.on_event("startup")
def load_model():
    global model
    model_path = config.BEST_MODEL_FILE
    print(f"Loading model from {model_path}...")
    
    if not model_path.exists():
        # Fallback for Docker/Cloud if model isn't built yet, or handle via S3 download strictly
        # For now, we assume the model exists or will be downloaded.
        print(f"WARNING: Model file not found at {model_path}")
        return

    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Music Recommender API. Use /predict to get recommendations."}

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    if not model:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # Preprocess input (Basic cleaning matching training)
    # Ideally, import clean_text from clean_transform, but let's keep it simple or import it
    # For robust engineering, we should import the exact function.
    
    try:
        # Assuming the pipeline handles vectorization internally (which it does)
        prediction = model.predict([request.text])[0]
        
        # If model supports proba
        confidence = 0.0
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba([request.text])
            confidence = float(max(probs[0]))

        return PredictionResponse(category=str(prediction), confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
