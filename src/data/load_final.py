import pandas as pd
import os
import sys
import boto3
from pathlib import Path

# Add src to python path to import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def load_final():
    print("Starting Final Data Loading...")
    
    input_path = config.CLEAN_DATA_FILE
    parquet_path = config.FINAL_DATA_PARQUET
    
    if not input_path.exists():
        print(f"Error: Processed file not found at {input_path}")
        return

    df = pd.read_csv(input_path)
    print(f"Data loaded from processed. Shape: {df.shape}")
    
    os.makedirs(config.FINAL_DATA_DIR, exist_ok=True)
        
    df.to_parquet(parquet_path, index=False)
    print(f"Data saved as Parquet: {parquet_path}")

    # --- AWS S3 UPLOAD ---
    if os.getenv("ENV") == "AWS":
        print(f"\n[AWS] Attempting upload to S3 Bucket: {config.S3_BUCKET_NAME}...")
    try:
        s3 = boto3.client('s3')
        s3.upload_file(
            Filename=str(parquet_path),
            Bucket=config.S3_BUCKET_NAME,
            Key=config.S3_DATA_FINAL_KEY
        )
        print(f"[AWS] Success! Data uploaded to s3://{config.S3_BUCKET_NAME}/{config.S3_DATA_FINAL_KEY}")
    except Exception as e:
        print(f"[AWS] Upload skipped or failed: {e}")
        print("Tip: Ensure you have run 'aws configure' or set AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY env vars.")

    print("Final loading complete.")

if __name__ == "__main__":
    load_final()
