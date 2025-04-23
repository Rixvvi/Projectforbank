import re
from collections import Counter


def get_search_str(operation: list[dict], string_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    result = []
    for i in operation:
        if re.search(rf'{string_search}', i['description'], flags=re.IGNORECASE):
            result.append(i)
    return result


operation = [
    {'id': 650703, 'state': 'EXECUTED', 'description': 'Перевод организации'},
    {'id': 3598919, 'state': 'EXECUTED', 'description': 'Открытие счета'},
    {'id': 593027, 'state': 'CANCELED', 'description': 'Перевод с карты на карту'},
    {'id': 366176, 'state': 'EXECUTED', 'description': 'Перевод с карты на карту'},
    {'id': 5380041, 'state': 'CANCELED', 'description': 'Открытие вклада'}
]

print(get_search_str(operation, 'Открытие'))


def get_categories(operation: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    result = []
    for i in operation:
        if i['description'] in categories:
            result.append(i['description'])
    counted = Counter(result)
    return counted


categories = ['Открытие счета', 'Открытие вклада']

print(get_categories(operation, categories))
