# pre-commits

Run checks like code formatting, style enforcement, and syntax validation to ensure code quality and consistency before it is committed. This prevents errors, maintains standards, and saves time on later processes like continuous integration.

- black - code formatter
- flake8 - code quality
- isort - sort imports
- bandit - for security
- commitizen - for commit messages

# Processing tools

- pandas
- polars
- duckdb
- dask

# Quality tools

- pydantic - row by row or API
- pandera - SQL, DataFrame

# JSON

Java Script Object Notation (JSON) - similar to python dictionary structure

# if **name** == "**main**"

Use this to test modules while implementing them, this can be used later for unit tests.

# LOG

Persists errors so they can be seen later

python log libraries:

- loguru
- logging
- sentry

# DECORATOR

Decorators in Python are a powerful feature that allow you to modify or enhance functions, methods, or classes without permanently changing the original code. They're essentially functions that take another function as input and return a modified version.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

## Examples

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()  # Output: slow_function took 2.00 seconds
```

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(5, 3)
```
