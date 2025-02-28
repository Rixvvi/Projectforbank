import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('first, second', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 35383033474447895560', 'Счет **5560')
])

def test_get_mask_card_number(first, second):
    assert mask_account_card(first) == second

def test_mask_card_number_with_not_str():
    with pytest.raises(AttributeError) as exc_info:
        mask_account_card(5)


@pytest.mark.parametrize('frst, scnd', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-02-28', '28.02.2025'),
    ('', 'Введена пустая строка')
])


def test_get_date(frst, scnd):
    assert get_date(frst) == scnd
