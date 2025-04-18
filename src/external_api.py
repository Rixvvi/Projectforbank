import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_external_api(transaction: list[dict]) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if 'operationAmount' not in transaction:
        return 0
    operation_amount = transaction['operationAmount']
    if 'currency' not in operation_amount:
        return 0
    currency = operation_amount['currency']
    if 'code' not in currency:
        return 0
    code = currency['code']
    if 'amount' not in operation_amount:
        return 0
    amount = operation_amount['amount']

    if code == 'RUB':
        return float(amount)

    if code in ['USD', 'EUR']:
        try:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

            headers = {
                "apikey": os.getenv('API_KEY')
            }

            response = requests.get(url, headers=headers, data={})

            result = response.json()

            if 'result' in result:
                return float(result['result'])

        except Exception as e:
            print(e.__class__.__name__)

    return float(0)


v = [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

print(get_external_api(v))
