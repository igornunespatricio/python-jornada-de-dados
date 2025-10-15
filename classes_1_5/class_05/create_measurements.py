import os
import random
import sys
import time

from config import CSV_PATH, NUMBER_ROWS_CREATE, TXT_PATH
from utils import write_statistics_to_file


def check_args(file_args):
    """
    Sanity checks out input and prints out usage if input is not a positive integer
    """
    try:
        if len(file_args) != 2 or int(file_args[1]) <= 0:
            raise Exception()
    except Exception:
        print(
            "Usage:  create_measurements.sh <positive "
            "integer number of records to create>",
        )
        print("        You can use underscore notation for large number of records.")
        print("        For example:  1_000_000_000 for one billion")
        exit()


def build_weather_station_name_list():
    """
    Grabs the weather station names from example data provided in repo and dedups
    """
    station_names = []
    with open(CSV_PATH, encoding="utf-8") as file:
        file_contents = file.read()
    for station in file_contents.splitlines():
        if "#" in station:
            next
        else:
            station_names.append(station.split(";")[0])
    return list(set(station_names))


def convert_bytes(num):
    """
    Convert bytes to a human-readable format (e.g., KiB, MiB, GiB)
    """
    for x in ["bytes", "KiB", "MiB", "GiB"]:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def format_elapsed_time(seconds):
    """
    Format elapsed time in a human-readable format
    """
    if seconds < 60:
        return f"{seconds:.3f} seconds"
    elif seconds < 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
    else:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes == 0:
            return f"{int(hours)} hours {int(seconds)} seconds"
        else:
            return f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"


def estimate_file_size(weather_station_names, num_rows_to_create):
    """
    Tries to estimate how large a file the test data will be
    """
    max_string = float("-inf")
    min_string = float("inf")
    per_record_size = 0

    for station in weather_station_names:
        max_string = max(max_string, len(station))
        min_string = min(min_string, len(station))
        per_record_size = ((max_string + min_string * 2) + len(",-123.4")) / 2

    total_file_size = num_rows_to_create * per_record_size
    human_file_size = convert_bytes(total_file_size)

    return f"""O tamanho estimado do arquivo é:  {human_file_size}.\nO tamanho
    final será provavelmente muito menor (metade)."""


def build_test_data(weather_station_names, num_rows_to_create):
    """
    Generates and writes to file the requested length of test data
    """
    start_time = time.time()
    coldest_temp = -99.9
    hottest_temp = 99.9
    station_names_10k_max = random.choices(weather_station_names, k=10_000)
    batch_size = 10000  # process a batch of stations and put it to disk
    max(1, (num_rows_to_create // batch_size) // 100)
    print("Criando o arquivo... isso vai demorar uns 10 minutos...")

    try:
        with open(TXT_PATH, "w", encoding="utf-8") as file:
            for s in range(0, num_rows_to_create // batch_size):

                batch = random.choices(station_names_10k_max, k=batch_size)
                prepped_deviated_batch = "\n".join(
                    [
                        f"{station};{random.uniform(coldest_temp, hottest_temp):.1f}"
                        for station in batch
                    ],
                )  # :.1f should quicker than round on a large scale
                file.write(prepped_deviated_batch + "\n")

        sys.stdout.write("\n")
    except Exception as e:
        print("Something went wrong. Printing error info and exiting...")
        print(e)
        exit()

    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize(TXT_PATH)
    human_file_size = convert_bytes(file_size)

    print(f"Arquivo escrito com sucesso {TXT_PATH}")
    print(f"Tamanho final:  {human_file_size}")
    print(f"Tempo decorrido: {format_elapsed_time(elapsed_time)}")
    write_statistics_to_file(__file__, format_elapsed_time(elapsed_time))


def main():
    """
    main program function
    """
    num_rows_to_create = NUMBER_ROWS_CREATE
    weather_station_names = []
    weather_station_names = build_weather_station_name_list()
    print(estimate_file_size(weather_station_names, num_rows_to_create))
    build_test_data(weather_station_names, num_rows_to_create)
    print("Arquivo de teste finalizado.")


if __name__ == "__main__":
    main()
