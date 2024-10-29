import logging

# Настройка логгера
logger = logging.getLogger("migration_logger")
logger.setLevel(logging.INFO)

# Логирование в файл
file_handler = logging.FileHandler('migration.log')
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

# Логирование в стандартный поток контейнера (stdout)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

# Добавляем обработчики в логгер
logger.addHandler(file_handler)
logger.addHandler(console_handler)
