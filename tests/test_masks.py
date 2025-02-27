import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value', 'expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('ghbdht', 'Введите номер карты'),
    ('5епроа', 'Введите номер карты'),
    ('10328476', 'Введите 16-ти значный номер карты'),
    ('', 'Введите номер карты'),
    ('1537289054628190453627' , 'Введите 16-ти значный номер карты')
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_account():
    assert get_mask_account(account = "13246158793614207463") == "**7463"
    assert get_mask_account(account="4536") == "Введите 20-ти значный номер счета"
    assert get_mask_account(account="онннеу") == "Введите номер счета"
    assert get_mask_account(account="4ук6рц") == "Введите номер счета"
    assert get_mask_account(account="") == "Введите номер счета"
