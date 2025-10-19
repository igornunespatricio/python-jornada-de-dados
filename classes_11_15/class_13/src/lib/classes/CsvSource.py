import os
import pandas as pd
from lib.classes.FilesSources import FilesSources


class CsvSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(
            current_directory, "classes_11_15", "class_13", "data", "csv_files"
        )
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [
            file
            for file in current_files
            if file not in self.previous_files and file.endswith(".csv")
        ]
        if new_files:
            print(f"New CSV files found:", new_files)
            self.previous_files = current_files
        else:
            print("No new CSV files found.")
            self.get_data()

    def get_data(self):
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = f"{self.folder_path}/{file_path}"
                df = pd.read_csv(path)
                data_frames.append(df)
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
        if data_frames:
            self.combined_data = pd.concat(data_frames, ignore_index=True)
            print(self.combined_data)
            return self.combined_data
        else:
            return None

    def transform_data_to_df(self):
        return super().transform_data_to_df()
