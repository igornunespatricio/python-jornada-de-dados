from etl import consolidated_etl

data_path: str = "classes_6_10/project_class_09/data"
output_file_format: str = "parquet"  # or "csv" or "both"

consolidated_etl(data_path=data_path, output_file_format=output_file_format)
