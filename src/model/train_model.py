import pandas as pd
import pickle
import json
import os
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def train_and_evaluate():
    print("Starting Model Training Pipeline...")
    
    input_path = config.FINAL_DATA_PARQUET
    
    # AWS S3 Data Retrieval
    if input_path.exists():
        pass 
    elif os.getenv("ENV") == "AWS":
        import boto3
        try:
            s3 = boto3.client('s3')
            os.makedirs(input_path.parent, exist_ok=True)
            s3.download_file(config.S3_BUCKET_NAME, config.S3_DATA_FINAL_KEY, str(input_path))
        except Exception as e:
            print(f"S3 Download Error: {e}")

    if not input_path.exists():
        print(f"Error: Final data not found at {input_path}")
        return
        
    df = pd.read_parquet(input_path)
    print(f"Data loaded. Shape: {df.shape}")
    
    df = df.dropna(subset=['cleaned_text', 'category'])
    X = df['cleaned_text']
    y = df['category']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = [
        {
            "name": "LogisticRegression",
            "pipeline": Pipeline([
                ('tfidf', TfidfVectorizer(max_features=5000)),
                ('clf', LogisticRegression(max_iter=1000))
            ])
        },
        {
            "name": "RandomForest",
            "pipeline": Pipeline([
                ('tfidf', TfidfVectorizer(max_features=5000)),
                ('clf', RandomForestClassifier(n_estimators=50, random_state=42))
            ])
        }
    ]
    
    best_accuracy = 0
    best_model = None
    best_model_name = ""
    results = {}
    
    for model_info in models:
        print(f"\nTraining {model_info['name']}...")
        pipe = model_info['pipeline']
        pipe.fit(X_train, y_train)
        
        y_pred = pipe.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{model_info['name']} Accuracy: {acc:.4f}")
        
        results[model_info['name']] = {
            "accuracy": acc,
            "report": classification_report(y_test, y_pred, output_dict=True)
        }
        
        if acc > best_accuracy:
            best_accuracy = acc
            best_model = pipe
            best_model_name = model_info['name']
            
    print(f"\nBest Model: {best_model_name} with Accuracy: {best_accuracy:.4f}")
    
    os.makedirs(config.MODELS_DIR, exist_ok=True)
        
    # Save Model
    with open(config.BEST_MODEL_FILE, 'wb') as f:
        pickle.dump(best_model, f)
    print(f"Best model saved to {config.BEST_MODEL_FILE}")

    # AWS Model Upload
    if os.getenv("ENV") == "AWS":
        import boto3
        try:
            s3 = boto3.client('s3')
            s3.upload_file(str(config.BEST_MODEL_FILE), config.S3_BUCKET_NAME, config.S3_MODEL_KEY)
        except Exception as e:
            print(f"Upload Error: {e}")
    
    # Save Metrics
    with open(config.METRICS_FILE, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Performance metrics saved to {config.METRICS_FILE}")

if __name__ == "__main__":
    train_and_evaluate()
