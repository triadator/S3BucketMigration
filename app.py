import logging
from minio_client import *
from migrate import *

# Настройка логирования
logging.basicConfig(
    filename='migration.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":

    minio_client = create_minio_client()
    
    create_buckets(minio_client, ["ispace"])

    migrate_files(minio_client)
    migrate_attachments(minio_client)
