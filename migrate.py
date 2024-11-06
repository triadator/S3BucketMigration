from minio import Minio
from minio.commonconfig import CopySource
from minio.error import S3Error
import logging

def migrate_objects(minio_client: Minio, bucket_name: str, new_path_template: str):
    """Миграция объектов из указанного бакета в новый путь."""
    for obj in minio_client.list_objects(bucket_name, recursive=True):
        # Делим старый ожидаемый шаблон пути на 4 части 
        # {site_id}/{list/library_id}/{item_id}/{file/attachment_name}
        parts = obj.object_name.split('/')
        
        if len(parts) == 4:
            new_path = new_path_template.format(*parts[:4])
            source = CopySource(bucket_name, obj.object_name)

            try:
                minio_client.copy_object("ispace", new_path, source)
                logging.info(f"Объект {obj.object_name} успешно скопирован в {new_path}")
            except S3Error as err:
                logging.error(f"Ошибка при копировании объекта {obj.object_name}: {err}")
            except Exception as e:
                logging.error(f"Неизвестная ошибка при копировании объекта {obj.object_name}: {e}")
        else:
            # Если имя не соотвествует старому ожидаемому шаблону, то прилетит ошибка.
            logging.error(f"Неверный формат имени объекта {obj.object_name}: ожидается как минимум 4 части, получено {len(parts)}")

def migrate_files(minio_client: Minio):
    """Миграция файлов из бакета 'files'."""
    new_path_template = "sites/{}/libraries/{}/files/{}/{}"
    migrate_objects(minio_client, "files", new_path_template)

def migrate_attachments(minio_client: Minio):
    """Миграция вложений из бакета 'attachments'."""
    new_path_template = "sites/{}/lists/{}/items/{}/attachments/{}"
    migrate_objects(minio_client, "attachments", new_path_template)
