import csv

import pandas as pd


def read_csv(file_path: str) -> list[dict]:
    """Функция, которая считывает финансовые операции из CSV выдает список словарей с транзакциями"""
    try:
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            data = list(reader)
        return data
    except Exception as e:
        print(e.__class__.__name__)

    return []


def read_from_excel(path: str) -> list[dict]:
    """Функция, которая считывает финансовые операции из XLSX выдает список словарей с транзакциями"""

    try:
        df = pd.read_excel(path)
        data = df.to_dict(orient='records')
        return data
    except Exception as e:
        print(e.__class__.__name__)

    return []
