from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    name_card = account_card.split(" ")
    if name_card[0] == "Счет":
        result = get_mask_account(name_card[-1])
    else:
        result = get_mask_card_number(name_card[-1])
    del name_card[-1]
    return " ".join(name_card) + " " + result


mask_account_card(input())


def get_date(date: str) -> str:
    """принимает на вход строку с датой и возвращает её в другом формате"""
    user_date = list()
    counter = 0
    day = ""
    our_date = date.split("-")

    for litera in our_date[2]:
        day += litera
        counter += 1
        if counter == 2:
            break

    user_date.append(day)
    user_date.append(our_date[1])
    user_date.append(our_date[0])

    return ".".join(user_date)


get_date(input())
