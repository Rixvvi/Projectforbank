from src.decorators import log, addiction
import pytest


def test_addiction_with_params():
    addiction(6, 7)
    with open("tests\mylog.txt", 'r', encoding="UTF-8") as file:
        content = file.readlines()
        assert(content[-1])