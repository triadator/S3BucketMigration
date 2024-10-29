from minio import Minio
from config import MINIO_CS, MINIO_ACCESS_KEY, MINIO_SECRET_KEY

def create_minio_client():
    return Minio(
            endpoint=MINIO_CS,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False
        )

def create_buckets(minio_client: Minio, bucket_names: list[str]):
    for bucket_name in bucket_names:
        if not minio_client.bucket_exists(bucket_name):
               minio_client.make_bucket(bucket_name)
