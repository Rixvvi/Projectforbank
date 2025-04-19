import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_external_api(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
        amount = transaction.get("operationAmount", {}).get("amount", 0)
        if code == "RUB":
            return float(amount)

        if code in ["USD", "EUR"]:
            try:
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

                headers = {"apikey": os.getenv("API_KEY")}

                response = requests.get(url, headers=headers, data={})

                result = response.json()

                if "result" in result:
                    return float(result["result"])

            except Exception as e:
                print(e.__class__.__name__)

    except Exception as e:
        print(e.__class__.__name__)

    return float(0)


v = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}

print(get_external_api(v))
