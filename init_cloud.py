import boto3
import os
import sys
from pathlib import Path

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))
import src.config as config

def bootstrap_s3():
    print(f"=== INITIALISATION CLOUD: Uploading Raw Data to {config.S3_BUCKET_NAME} ===")
    
    # 1. Vérifier le fichier local
    local_file = config.LOCAL_SOURCE_FILE
    if not local_file.exists():
        print(f"ERREUR: Fichier introuvable sur votre PC: {local_file}")
        return

    # 2. Upload vers S3
    s3_key = config.S3_DATA_RAW_KEY # "data/raw/bbc-news-data.csv"
    
    print(f"Source: {local_file}")
    print(f"Destination: s3://{config.S3_BUCKET_NAME}/{s3_key}")
    
    try:
        s3 = boto3.client('s3')
        s3.upload_file(str(local_file), config.S3_BUCKET_NAME, s3_key)
        print("\n✅ SUCCÈS ! Les données brutes sont sur S3.")
        print("Maintenant, GitHub Actions pourra les télécharger pour entraîner le modèle.")
    except Exception as e:
        print(f"\n❌ ERREUR: Impossible de se connecter à AWS.")
        print(f"Détail: {e}")
        print("\nASTUCE: Avez-vous défini vos variables d'environnement dans ce terminal ?")
        print('$env:AWS_ACCESS_KEY_ID="..."')
        print('$env:AWS_SECRET_ACCESS_KEY="..."')

if __name__ == "__main__":
    bootstrap_s3()
