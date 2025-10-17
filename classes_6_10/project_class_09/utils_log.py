from loguru import logger
from functools import wraps

logger.add(
    sink="classes_6_10/project_class_09/log.log",
    format="{time} {level} {file} {message}",
    level="INFO",
)

logger.add(
    sink="classes_6_10/project_class_09/critical.log",
    format="{time} {level} {file} {message}",
    level="ERROR",
)


def log_decorator(func):
    """Decorator to log function calls and exceptions."""

    @wraps(func)  # Preserve the original function's metadata
    def wrapper(*args, **kwargs):
        """Wrapper function to log function calls and exceptions."""
        logger.info(
            f"Calling function {func.__name__} with args {args} and kwargs {kwargs}"
        )
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} returned {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception in {func.__name__}: {e}")
            raise

    return wrapper
