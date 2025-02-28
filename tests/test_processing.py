from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(transaction_requests_executed: list[dict]) -> None:
    for trans in transaction_requests_executed:
        a, b, c = trans
        assert filter_by_state(a, b) == c


def test_filter_by_state_canceled(transaction_requests_canceled: list[dict]) -> None:
    for transaction in transaction_requests_canceled:
        e, m, d = transaction
        assert filter_by_state(e, m) == d


def test_filter_by_state_nothing(transaction_requests_canceled_nothing: list[dict]) -> None:
    for trill in transaction_requests_canceled_nothing:
        q, n = trill
        assert filter_by_state(q) == n


def test_sort_by_date_true(function_1: list[dict]) -> None:
    for fan in function_1:
        one, two = fan
        assert sort_by_date(one) == two


def test_sort_by_date_similar(function_2: list[dict]) -> None:
    for naf in function_2:
        eno, owt = naf
        assert sort_by_date(eno) == owt


def test_sort_by_date_non_standard(function_3: list[dict]) -> None:
    for pin in function_3:
        avna, owna = pin
        assert sort_by_date(avna) == owna


def test_sort_by_date_false(function_4: list[dict]) -> None:
    for pictur in function_4:
        aghj, pokg, trew = pictur
        assert sort_by_date(aghj, pokg) == trew
