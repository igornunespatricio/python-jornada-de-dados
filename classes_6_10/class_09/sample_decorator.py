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


def repeat(num_times):
    """Decorator to repeat a function multiple times."""
    print(f"repeat decorator {num_times} times")

    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


def singleton(cls):
    """Decorator to make a class a singleton."""
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
