from logger_setup import *
from minio_client import *
from migrate import *

if __name__ == "__main__":

    minio_client = create_minio_client()
    
    create_buckets(minio_client, ["ispace"])
    logger.info("ISpace Bucket is created.")
    logger.info("Starting migration process.")
    migrate_files(minio_client)
    migrate_attachments(minio_client)
    logger.info("Migration process completed.")
