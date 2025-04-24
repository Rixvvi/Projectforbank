from src.data_reading import read_csv, read_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reg_exp import get_search_str
from src.utils import read_json
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""

    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

    while True:
        type_file = input()
        if type_file == '1':
            transactions = read_json('../data/operations.json')
            print('Для обработки выбран JSON-файл.')
            break
        elif type_file == '2':
            transactions = read_csv('../data/transactions.csv')
            print('Для обработки выбран CSV-файл.')
            break
        elif type_file == '3':
            transactions = read_from_excel('../data/transactions_excel.xlsx')
            print('Для обработки выбран XLSX-файл.')
            break
        else:
            print('Выберите число от 1 до 3.')

    print('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    while True:
        possible = ['EXECUTED', 'CANCELED', 'PENDING']
        choice = input().strip()
        if choice.upper() in possible:
            transac = filter_by_state(transactions, choice.upper())
            print(f'Операции отфильтрованы по статусу "{choice.upper()}"')
            break
        else:
            print(f'Статус операции "{choice}" недоступен.')

    while True:
        choice = input('Отсортировать операции по дате? Да/Нет: ').lower().strip()
        if choice == 'нет':
            tran = transac
            break
        elif choice == 'да':
            while True:
                us_input = input('Отсортировать по возрастанию или по убыванию? ').lower().strip()
                if us_input == 'по возрастанию':
                    tran = sort_by_date(transac, False)
                    break
                elif us_input == 'по убыванию':
                    tran = sort_by_date(transac)
                    break
                else:
                    print('Некорректный ввод.')
            break
        else:
            print('Некорректный ввод.')

    while True:
        choice = input('Выводить только рублевые транзакции? Да/Нет: ').lower().strip()
        if choice in ("да", "нет"):
            if choice == "да" and type_file == "1":
                tran = [transaction for transaction in filter_by_currency(tran, 'RUB')]
            elif choice == "да":
                tran = list(filter(lambda x: x["currency_code"] == "RUB", tran))
            break
        else:
            print('Некорректный ввод.')

    while True:
        choice = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ').lower().strip()
        if choice == 'да':
            us_input = input('Введите слово, по которому вы бы хотели отфильтровать список транзакций: ')
            operat = get_search_str(tran, us_input)
            break
        elif choice == 'нет':
            operat = tran
            break
        else:
            print('Некорректный ввод.')

    print('Распечатываю итоговый список транзакций...')

    if len(operat):
        print(f'Всего банковских операций в выборке: {len(operat)}')

        for o in operat:

            date = get_date(o.get("date", ""))

            description = o.get("description", "")

            if 'currency_code' in o:
                code = o.get("currency_code", "")
                amount = float(o.get("amount", 0))
            else:
                code = o.get("operationAmount", {}).get("currency", {}).get("code", "")
                amount = float(o.get("operationAmount", {}).get("amount", 0))

            if code == 'RUB':
                code = 'руб.'

            to_masked = mask_account_card(o.get("to", ""))
            from_mask = o.get("from")

            if from_mask:
                from_masked = mask_account_card(from_mask)
                direction = f"{from_masked} -> {to_masked}"
            else:
                direction = f"{to_masked}"

            print(f"{date} {description}\n{direction}\nСумма: {int(amount)} {code}")
            print()
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')


if __name__ == "__main__":
    main()
