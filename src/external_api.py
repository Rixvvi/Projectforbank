import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_external_api(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        if 'currency_code' in transaction:
            code = transaction.get("currency_code", {})
            amount = transaction.get("amount", {})
        else:
            code = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
            amount = transaction.get("operationAmount", {}).get("amount", 0)
        if code == "RUB":
            return float(amount)

        else:
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
