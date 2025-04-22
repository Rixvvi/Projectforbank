import csv
import pandas as pd


def read_csv(file_path):
    try:
        with open(file_path) as file:
            reader = csv.DictReader(file, delimiter=';')
            data = list(reader)
        return data
    except Exception as e:
        print(e.__class__.__name__)

print(read_csv('../data/transactions.csv'))


def read_excel(path):
    pass
