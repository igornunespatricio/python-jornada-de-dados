import pandas as pd


class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.filtered_df = None

    def load_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filter_column(self, column_name: str, value: str):
        self.filtered_df = self.df[self.df[column_name] == value]
        return self.filtered_df

    def sub_filter_column(self, column_name: str, value: str):
        return self.filtered_df[self.filtered_df[column_name] == value]

    def recursive_filters(self, columns: list, values: list):
        if len(columns) != len(values):
            raise ValueError("Columns and values must have the same length")
        if len(columns) == 0:
            return self.df

        current_column = columns[0]
        current_value = values[0]
        filtered_df = self.df.copy()
        filtered_df = filtered_df[filtered_df[current_column] == current_value]

        if len(columns) == 1:
            return filtered_df
        else:
            return self.recursive_filters(columns[1:], values[1:])
