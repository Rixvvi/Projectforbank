import json
import logging
from json import JSONDecodeError
from typing import Any

my_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/log_utils.log', 'w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.DEBUG)


def read_json(path: str) -> Any:
    """Функция, принимающая на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                my_logger.error('Все успешно')
                return data
    except FileNotFoundError:
        my_logger.error('Файл не найден')
        return []
    except JSONDecodeError:
        my_logger.error('Ошибка при чтении файла')
        return []
