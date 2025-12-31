import os
import shutil
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def download_data():

    print("Starting data ingestion...")
    
    # Ensure directory exists
    os.makedirs(config.RAW_DATA_DIR, exist_ok=True)
        
    dest_path = config.RAW_DATA_FILE
    
    if os.getenv("ENV") == "AWS":
        import boto3
        try:
            print(f"Downloading from S3: s3://{config.S3_BUCKET_NAME}/{config.S3_DATA_RAW_KEY}")
            s3 = boto3.client('s3')
            s3.download_file(config.S3_BUCKET_NAME, config.S3_DATA_RAW_KEY, str(dest_path))
        except Exception as e:
            print(f"[AWS] S3 Download Failed: {e}")
            print("Attempting local fallback for CI/CD initialization...")
            source_path = config.LOCAL_SOURCE_FILE
            if source_path.exists():
                shutil.copy2(source_path, dest_path)
                print(f"Fallback: Scaled from {source_path} to {dest_path}")
            else:
                print("FATAL: No data found in S3 or local directory.")
                raise e
    else:
        source_path = config.LOCAL_SOURCE_FILE
        if source_path.exists():
            shutil.copy2(source_path, dest_path)
            print(f"Data successfully copied from {source_path} to {dest_path}")
        else:
            print(f"Error: Source file not found at {source_path}")

if __name__ == "__main__":
    download_data()
