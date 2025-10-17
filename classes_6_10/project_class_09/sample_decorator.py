from functools import wraps
import time

from functools import wraps


def print_hello(func):
    """Decorator to print 'Hello' before calling the function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)

    return wrapper


def timer_decorator(func):
    """Decorator to measure the time taken by a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took {end_time - start_time} seconds to execute."
        )
        return result

    return wrapper
