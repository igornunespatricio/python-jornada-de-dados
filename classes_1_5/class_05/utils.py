import os

from config import STATISTICS_FILE_PATH


def write_statistics_to_file(
    filepath: str,
    time: str,
) -> None:
    if not os.path.exists(STATISTICS_FILE_PATH):
        mode = "w"
    else:
        mode = "a"
    with open(STATISTICS_FILE_PATH, mode, encoding="utf-8") as file:
        file.write(f"{filepath}, {time}\n")


def print_statistics_file():
    print("\nStatistics:")
    with open(STATISTICS_FILE_PATH, "r", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    print_statistics_file()
