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
    for func1_1 in function_1:
        f1_1, f_1 = func1_1
        assert sort_by_date(f1_1) == f_1


def test_sort_by_date_similar(function_2: list[dict]) -> None:
    for func2_2 in function_2:
        f2_2, f_2 = func2_2
        assert sort_by_date(f2_2) == f_2


def test_sort_by_date_non_standard(function_3: list[dict]) -> None:
    for func3_3 in function_3:
        f3_3, f_3 = func3_3
        assert sort_by_date(f3_3) == f_3


def test_sort_by_date_false(function_4: list[dict]) -> None:
    for func4_4 in function_4:
        f4_4, arg_for_func, f_4 = func4_4
        assert sort_by_date(f4_4, arg_for_func) == f_4
