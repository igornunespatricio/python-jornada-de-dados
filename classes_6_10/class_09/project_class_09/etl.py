"""Functions to do the ETL."""

import glob
import os

import pandas as pd
from utils_log import log_decorator


@log_decorator
def extract_data(path: str) -> pd.DataFrame:
    """Extract data from json files."""
    globs = os.path.join(path, "*.json")
    json_files = glob.glob(globs)
    list_dfs = [pd.read_json(file) for file in json_files]
    return pd.concat(list_dfs, ignore_index=True)


@log_decorator
def calculate_total_amount(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total amount = quantity * price."""
    df["total_amount"] = df["quantity"] * df["amount"]
    return df


@log_decorator
def load_data(
    df: pd.DataFrame,
    output_path: str,
    output_format: str,
) -> None:
    """Load data to .csv or .parquet or both."""
    if output_format == "csv":
        df.to_csv(os.path.join(output_path, "output_file.csv"), index=False)
    elif output_format == "parquet":
        df.to_parquet(os.path.join(output_path, "output_file.parquet"), index=False)
    elif output_format == "both":
        df.to_csv(os.path.join(output_path, "output_file.csv"), index=False)
        df.to_parquet(os.path.join(output_path, "output_file.parquet"), index=False)
    else:
        raise ValueError("Invalid output format")


@log_decorator
def consolidated_etl(
    data_path: str,
    output_file_format: str = "parquet",
):
    """
    Consolidate the ETL pipeline into a single function.

    Parameters
    ----------
    data_path : str, optional
        The path to the data directory. Defaults to "classes_6_10/project_class_08/data".
    output_file_format : str, optional
        The format of the output file. Can be "csv", "parquet" or "both". Defaults to "parquet".

    Returns
    -------
    None

    """
    raw_data = extract_data(data_path)
    transformed_data = calculate_total_amount(raw_data)
    load_data(transformed_data, data_path, output_file_format)


if __name__ == "__main__":
    data_path: str = "classes_6_10/class_09/project_class_09/data"
    raw_data = extract_data(data_path)
    transformed_data = calculate_total_amount(raw_data)
    output_file_format: str = "parquet"  # or "csv" or "both"
    load_data(transformed_data, data_path, output_file_format)
