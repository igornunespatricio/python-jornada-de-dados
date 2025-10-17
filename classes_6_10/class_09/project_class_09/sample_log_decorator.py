from utils_log import log_decorator


@log_decorator
def addition(a, b):
    return a + b


addition(3, 4)

addition(3, "test")
