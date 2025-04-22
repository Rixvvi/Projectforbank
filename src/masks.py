import logging

my_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/log_masks.log', 'w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    masked_card = list()
    if card_number.isdigit():
        if len(card_number) == 16:
            my_logger.debug('Успешно введен номер карты')
            for number in card_number[:6]:
                masked_card.append(str(number))
            for number in card_number[6:-4]:
                masked_card.append("*")
            for number in card_number[-4:]:
                masked_card.append(str(number))
            mask_card = "".join(masked_card)
            return " ".join(mask_card[i : i + 4] for i in range(0, len(mask_card), 4))
        else:
            my_logger.debug('Введен не 16-ти значный номер карты')
            return "Введите 16-ти значный номер карты"
    else:
        my_logger.debug('Введены не только цифры, но и иные символы')
        return "Введите номер карты"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_account = list()
    if account.isdigit():
        if len(account) == 20:
            my_logger.debug('Успешно введен номер счета')
            mask_account.append("**")
            for number in account[-4:]:
                mask_account.append(str(number))
            return "".join(mask_account)
        else:
            my_logger.debug('Введен не 20-ти значный номер счета')
            return "Введите 20-ти значный номер счета"
    else:
        my_logger.debug('Введены не только цифры, но и иные символы')
        return "Введите номер счета"
