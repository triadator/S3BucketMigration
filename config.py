import os

MINIO_CS = os.getenv("MINIO_CS")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

if MINIO_CS is None:
    raise EnvironmentError("Ошибка: Переменная окружения 'MINIO_CS' не установлена.")

if MINIO_ACCESS_KEY is None:
    raise EnvironmentError("Ошибка: Переменная окружения 'MINIO_ACCESS_KEY' не установлена.")

if MINIO_SECRET_KEY is None:
    raise EnvironmentError("Ошибка: Переменная окружения 'MINIO_SECRET_KEY' не установлена.")
