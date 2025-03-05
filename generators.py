from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict, None, None]:
    """Функция принимает на вход список словарей, представляющих транзакции, а затем возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in transactions:
        if 'operationAmount' not in transaction:
            continue
        operation_amount = transaction['operationAmount']
        if 'currency' not in operation_amount:
            continue
        currency = operation_amount['currency']
        if 'code' not in currency:
            continue
        code = currency['code']
        if currency_code == code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, None, None]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for trans in transactions:
        if 'description' not in trans:
            continue
        yield trans['description']


def card_number_generator(start: int, end: int) -> Generator[dict, None, None]:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for i in range(start, end + 1):
        result = str(i).rjust(16, '0')
        yield result[0:4] + ' ' + result[4:8] + ' ' + result[8:12] + ' ' + result[12:16]
