import json
from json import JSONDecodeError


def read_json(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
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
