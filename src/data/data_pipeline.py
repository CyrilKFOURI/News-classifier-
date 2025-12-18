import download_data
import clean_transform
import load_final

def run_data_pipeline():
    """
    Orchestrates the ETL Pipeline:
    1. Extract: Download data
    2. Transform: Clean and Preprocess
    3. Load: Save to final storage (Parquet/DB)
    """
    print("=== Starting AWS-Ready Data Pipeline ===")
    
    # Step 1: Extraction
    print("\n[Step 1/3] Downloading Data...")
    download_data.download_data()
    
    # Step 2: Transformation
    print("\n[Step 2/3] Cleaning and Transforming Data...")
    clean_transform.preprocess_data()
    
    # Step 3: Loading
    print("\n[Step 3/3] Loading Data to Final Storage...")
    load_final.load_final()
    
    print("\n=== Data Pipeline Completed Successfully ===")

if __name__ == "__main__":
    run_data_pipeline()
