import pandas as pd
import re
import os
import sys
from pathlib import Path

# Add src to python path to import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data():
    print("Starting data preprocessing...")
    
    input_path = config.RAW_DATA_FILE
    
    if not input_path.exists():
        print(f"Error: Input file not found at {input_path}")
        return

    try:
        df = pd.read_csv(input_path, sep='\t') 
    except:
        df = pd.read_csv(input_path)

    print(f"Data loaded. Shape: {df.shape}")
    
    if 'text' in df.columns:
        df['cleaned_text'] = df['text'].apply(clean_text)
    else:
        # Fallback
        for col in df.select_dtypes(include=['object']).columns:
             if col != 'category':
                 print(f"Using '{col}' as text column.")
                 df['cleaned_text'] = df[col].apply(clean_text)
                 break
    
    os.makedirs(config.PROCESSED_DATA_DIR, exist_ok=True)
    
    output_path = config.CLEAN_DATA_FILE
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data()
