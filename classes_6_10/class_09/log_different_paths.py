from loguru import logger
from sys import stderr

LOG_DIR = "classes_6_10/class_09/"


logger.add(
    sink=stderr,
    level="INFO",
    format="{time} {level} {file} {message}",
    filter=lambda record: record["level"].name == "INFO",
)

logger.add(
    sink=f"{LOG_DIR}critical.log",
    level="CRITICAL",
    format="{time} {level} {file} {message}",
    filter=lambda record: record["level"].name == "CRITICAL",
)

logger.add(
    sink=f"{LOG_DIR}warning.log",
    level="WARNING",
    format="{time} {level} {file} {message}",
    filter=lambda record: record["level"].name == "WARNING",
)


def addition(x: int, y: int) -> int:
    """Add two values."""
    try:
        result = int(x) + int(y)
        logger.info(f"{x} + {y} = {result}")
    except Exception as e:
        logger.critical(e)


addition(3, 4)

addition(3, "4")

addition(3, "test")

logger.warning("Finishing execution and  logging as warning.")
