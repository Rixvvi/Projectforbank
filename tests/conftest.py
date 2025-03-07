import pytest


@pytest.fixture()
def transaction_requests_executed() -> list[tuple]:
    filter_answers = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ]
    return filter_answers


@pytest.fixture()
def transaction_requests_canceled() -> list[tuple]:
    answer_filter = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ]
    return answer_filter


@pytest.fixture()
def transaction_requests_canceled_nothing() -> list[tuple]:
    filter_func = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ]
    return filter_func


@pytest.fixture()
def function_1() -> list[tuple]:
    func_1 = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ],
        ),
    ]
    return func_1


@pytest.fixture()
def function_2() -> list[tuple]:
    func_2 = [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ],
        ),
    ]
    return func_2


@pytest.fixture()
def function_3() -> list[tuple]:
    func_3 = [
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ],
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ],
        ),
    ]
    return func_3


@pytest.fixture()
def function_4() -> list[tuple]:
    func_4 = [
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ],
            False,
            [
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
            ],
        ),
    ]
    return func_4


@pytest.fixture()
def transactions() -> list[dict]:
    transactions = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )
    return transactions
