from _pytest.capture import CaptureFixture

from src.decorators import addiction, exception_interpreter, subtraction


def test_addiction_with_params() -> None:
    addiction(6, 7)
    with open("./mylog.txt", "w", encoding="UTF-8") as file:
        file.readlines()
        assert "addiction start"
        assert "addiction ok"


def test_subtraction(capsys: CaptureFixture[str]) -> None:
    subtraction()
    capsys.readouterr()
    assert "subtraction start"
    assert "subtraction ok"


def test_exception() -> None:
    addiction(6, 7)
    with open("./errors.txt", "w", encoding="UTF-8") as file:
        file.readlines()
        assert "exception start"
        assert "exception error: ZeroDivisionError. Inputs: 5 0"


def test_exception_interpreter(capsys: CaptureFixture[str]) -> None:
    exception_interpreter()
    capsys.readouterr()
    assert "exception_interpreter start"
    assert "exception_interpreter error: ValueError. Inputs: 6 Котик"
