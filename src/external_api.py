import requests
from src.utils import read_json


def external_api():
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    trans_file = read_json("../data/operations.json")
    counter = 0

    for transaction in trans_file:
        if 'operationAmount' not in transaction:
            continue
        operation_amount = transaction['operationAmount']
        if 'currency' not in operation_amount:
            continue
        currency = operation_amount['currency']
        if 'code' not in currency:
            continue
        code = currency['code']
        if 'amount' not in operation_amount:
            continue
        amount = operation_amount['amount']

        if code == 'RUB':
            counter += float(amount)

        if code in ['USD', 'EUR']:
            try:
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

                headers = {
                    "apikey": "arDZDYKt8dk1NxTnDcED60BCbExuAyeo"
                }

                response = requests.get(url, headers=headers, data={})

                result = response.json()

                for res in result:
                    if 'result' not in res:
                        continue
                    resultation = result['result']
                    counter += resultation

            except Exception as e:
                print(e.__class__.__name__)

    return counter


print(external_api())
