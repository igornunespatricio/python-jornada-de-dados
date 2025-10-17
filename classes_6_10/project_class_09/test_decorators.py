from sample_decorator import print_hello, timer_decorator
import time


@print_hello
def add(a, b):
    result = a + b
    print(result)
    return result


add(1, 2)


@timer_decorator
def test_time_decorator():
    j = 0
    for i in range(100000):
        j += i


test_time_decorator()
