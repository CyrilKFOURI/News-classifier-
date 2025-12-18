import download_data
import preprocess

def run_pipeline():
    """
    Orchestrates the entire data pipeline:
    1. Ingest/Download data
    2. Cleaner/Preprocess data
    """
    print("=== Starting Data Pipeline ===")
    
    # Step 1: Ingest
    print("\n[Step 1/2] Running Data Ingestion...")
    download_data.download_data()
    
    # Step 2: Preprocess
    print("\n[Step 2/2] Running Data Preprocessing...")
    preprocess.preprocess_data()
    
    print("\n=== Pipeline Completed Successfully ===")

if __name__ == "__main__":
    run_pipeline()
