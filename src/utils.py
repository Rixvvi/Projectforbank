import json
from json import JSONDecodeError
from typing import Any


def read_json(path: str) -> Any:
    """Функция, принимающая на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях"""
    try:
        with open(path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return []
        return data
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
