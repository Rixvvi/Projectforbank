from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Any:
    """Декоратор, который логирует начало, конец, результат и ошибки"""
    def decorator(func: Callable[..., Any]) -> Any:
        """Декоратор логирования начала, конца, результата и ошибок функции"""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Функция обертка"""
            start_message = f'{func.__name__} start'
            if filename:
                with open(filename, 'a') as file:
                    file.write(start_message + '\n')
            else:
                print(start_message)
            try:
                result = func(*args, **kwargs)
                end_message = f'{func.__name__} ok'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(end_message + '\n')
                else:
                    print(end_message)
                return result
            except Exception as e:
                error_message = f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(error_message + '\n')
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
