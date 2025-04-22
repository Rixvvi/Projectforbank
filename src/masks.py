def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    masked_card = list()
    if card_number.isdigit():
        if len(card_number) == 16:
            for number in card_number[:6]:
                masked_card.append(str(number))
            for number in card_number[6:-4]:
                masked_card.append("*")
            for number in card_number[-4:]:
                masked_card.append(str(number))
            mask_card = "".join(masked_card)
            return " ".join(mask_card[i : i + 4] for i in range(0, len(mask_card), 4))
        else:
            return "Введите 16-ти значный номер карты"
    else:
        return "Введите номер карты"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_account = list()
    if account.isdigit():
        if len(account) == 20:
            mask_account.append("**")
            for number in account[-4:]:
                mask_account.append(str(number))
            return "".join(mask_account)
        else:
            return "Введите 20-ти значный номер счета"
    else:
        return "Введите номер счета"
