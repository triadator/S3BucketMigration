docker build -t migration .
docker run -it --name migration --network ispace -e MINIO_CS="minio:9000" -e MINIO_ACCESS_KEY="" -e MINIO_SECRET_KEY="" migration
