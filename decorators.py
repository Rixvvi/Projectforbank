from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_message = f'Функция {func.__name__} началась с аргументами: {args} и {kwargs}'
            if filename:
                with open(filename, 'a') as file:
                    file.write(start_message + '\n')
            else:
                print(start_message)
            try:
                result = func(*args, **kwargs)
                end_message = f'Функция {func.__name__} завершилась с результатом: {result}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(end_message + '\n')
                else:
                    print(end_message)
                return result
            except Exception as e:
                error_message = f'Ошибка в функции {func.__name__}, тип ошибки: {type(e).__name__} с аргументами {args} и {kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(error_message + '\n')
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
