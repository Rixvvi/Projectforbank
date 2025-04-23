from src.data_reading import read_from_excel, read_csv
from src.utils import read_json
from src.processing import filter_by_state, sort_by_date


def main():

    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

    while True:
        user_input = int(input())
        if user_input == 1:
            transactions = read_json('../data/operations.json')
            print('Для обработки выбран JSON-файл.')
            break
        elif user_input == 2:
            transactions = read_csv('../data/transactions.csv')
            print('Для обработки выбран CSV-файл.')
            break
        elif user_input == 3:
            transactions = read_from_excel('../data/transactions_excel.xlsx')
            print('Для обработки выбран XLSX-файл.')
            break
        else:
            print('Выберите число от 1 до 3.')

    print('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    while True:
        possible = ['EXECUTED', 'CANCELED', 'PENDING']
        user_input = input()
        if user_input.upper() in possible:
            transac = filter_by_state(transactions, user_input.upper())
            print(f'Операции отфильтрованы по статусу "{user_input}"')
            break
        else:
            print(f'Статус операции "{user_input}" недоступен.')

    print('Отсортировать операции по дате? Да/Нет')

    while True:
        user_input = input().lower()
        if user_input == 'нет':
            break
        elif user_input == 'да':
            print('Отсортировать по возрастанию или по убыванию?')
            while True:
                us_input = input().lower()
                if us_input == 'по возрастанию':
                    tran = sort_by_date(transac, False)
                    break
                elif us_input == 'по убыванию':
                    tran = sort_by_date(transac)
                    break
                else:
                    print('Выберите способ сортировки: по возрастанию/по убыванию')
            break
        else:
            print('Некорректный ответ. Отсортировать операции по дате? Да/Нет')

    print('Выводить только рублевые транзакции? Да/Нет')

    while True:
        user_input = input.lower()

    #print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    #print('Распечатываю итоговый список транзакций...')
    #print('Всего банковских операций в выборке:')

    #print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

main()
