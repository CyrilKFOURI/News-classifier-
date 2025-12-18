import os
import shutil
import sys
from pathlib import Path

# Add src to python path to import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def download_data():
    """
    Simulates downloading data. 
    In the cloud, this would use boto3 to download from S3.
    """
    print("Starting data ingestion...")
    
    # Ensure directory exists
    os.makedirs(config.RAW_DATA_DIR, exist_ok=True)
        
    dest_path = config.RAW_DATA_FILE
    
    # --- LOGIC SELECTION: LOCAL vs CLOUD ---
    if os.getenv("ENV") == "AWS":
        # Cloud Logic
        import boto3
        s3 = boto3.client('s3')
        print(f"Downloading from S3: s3://{config.S3_BUCKET_NAME}/{config.S3_DATA_RAW_KEY}")
        s3.download_file(config.S3_BUCKET_NAME, config.S3_DATA_RAW_KEY, str(dest_path))
    else:
        # Local Logic (Simulation)
        source_path = config.LOCAL_SOURCE_FILE
        if source_path.exists():
            shutil.copy2(source_path, dest_path)
            print(f"Data successfully copied from {source_path} to {dest_path}")
        else:
            print(f"Error: Source file not found at {source_path}")

if __name__ == "__main__":
    download_data()
