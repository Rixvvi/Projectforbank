def filter_by_state(list_trans: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и значение state, после чего возвращает новый список словарей,
    содержащий только те словари, у которых ключ совпадает с введенным значением state"""
    new_list: list[dict] = []
    for trans in list_trans:
        if trans.get("state") == state:
            new_list.append(trans)
    return new_list


list_of_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

state = input()
if state != "EXECUTED" and state != "CANCELED":
    state = "EXECUTED"

filter_by_state(list_of_dictionaries, state)


def sort_by_date(requests: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и параметр, задающий порядок сортировки,
    и возвращает новый отсортированный список"""
    return sorted(requests, key=lambda x: x.get("date", ""), reverse=reverse)


list_of_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

sort_by_date(list_of_dictionaries)
