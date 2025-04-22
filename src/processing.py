def filter_by_state(list_trans: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и значение state, после чего возвращает новый список словарей,
    содержащий только те словари, у которых ключ совпадает с введенным значением state"""
    new_list: list[dict] = []
    for transaction in list_trans:
        if transaction.get("state") == state:
            new_list.append(transaction)
    return new_list


def sort_by_date(requests: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и параметр, задающий порядок сортировки,
    после чего возвращает новый отсортированный список"""
    return sorted(requests, key=lambda x: x.get("date", ""), reverse=reverse)
