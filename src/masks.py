def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    mask = list()

    for num in card_number[:6]:
        mask.append(str(num))

    for num in card_number[6:-4]:
        mask.append("*")

    for num in card_number[-4:]:
        mask.append(str(num))

    mask_card = "".join(mask)

    return " ".join(mask_card[i : i + 4] for i in range(0, len(mask_card), 4))


get_mask_card_number(input())


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_account = list()

    mask_account.append("**")

    for number in account[-4:]:
        mask_account.append(str(number))

    return "".join(mask_account)


get_mask_account(input())
