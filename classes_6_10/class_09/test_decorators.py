from sample_decorator import print_hello, repeat, singleton, timer_decorator


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


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Alice")  # Prints "Hello Alice" 3 times


@singleton
class Database:
    def __init__(self):
        print("Database created")


# Only one instance will be created
db1 = Database()
db2 = Database()  # Same instance as db1
