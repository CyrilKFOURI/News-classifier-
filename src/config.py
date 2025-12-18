import os
from pathlib import Path

# --- Base Directory Inference ---
# Returns the project root directory regardless of where the code is run from
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --- Directory Structure ---
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FINAL_DATA_DIR = DATA_DIR / "final"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOK_DIR = PROJECT_ROOT / "Notebook"

# --- File Paths ---
# Input/Output definitions
RAW_DATA_FILE = RAW_DATA_DIR / "bbc-news-data.csv"
CLEAN_DATA_FILE = PROCESSED_DATA_DIR / "clean_data.csv"
FINAL_DATA_PARQUET = FINAL_DATA_DIR / "music_recommender_data.parquet"
BEST_MODEL_FILE = MODELS_DIR / "best_model.pkl"
METRICS_FILE = MODELS_DIR / "metrics.json"

# --- Simulation / Local Dev Sources ---
LOCAL_SOURCE_FILE = NOTEBOOK_DIR / "bbc-news-data.csv"

# --- AWS Configuration ---
# Remplacez 'votre-bucket-name' par le nom réel de votre bucket si vous n'utilisez pas de variable d'environnement
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "votre-bucket-name") 

# Paths in S3
S3_DATA_RAW_KEY = "data/raw/bbc-news-data.csv"
S3_DATA_FINAL_KEY = "data/final/music_recommender_data.parquet"
S3_MODEL_KEY = "models/best_model.pkl"
