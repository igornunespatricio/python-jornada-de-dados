from interface.classes.csv_class import CsvProcessor


CSV_PATH = "classes_11_15/class_12/example.csv"
STATE = "CA"
COLUMN_NAME = "state"
SUB_FILTER_COLUMN = "price"
PRICE = 199.99

CSV_PATH_2 = "classes_11_15/class_12/example_2.csv"
STATE_2 = "RJ"
COLUMN_NAME_2 = "state"
SUB_FILTER_COLUMN_2 = "price"
PRICE_2 = 200


csv_processor = CsvProcessor(CSV_PATH)
csv_processor.load_csv()
df_filter = csv_processor.filter_column(COLUMN_NAME, STATE)
sub_df_filter = csv_processor.sub_filter_column(SUB_FILTER_COLUMN, PRICE)
print(df_filter)
print(sub_df_filter)


csv_processor2 = CsvProcessor(CSV_PATH_2)
csv_processor2.load_csv()
df_filter2 = csv_processor2.filter_column(COLUMN_NAME_2, STATE_2)
sub_df_filter2 = csv_processor2.sub_filter_column(SUB_FILTER_COLUMN_2, PRICE_2)
print(df_filter2)
print(sub_df_filter2)

# using recursive filters
columns = [COLUMN_NAME, SUB_FILTER_COLUMN]
values = [STATE, PRICE]
recursive_df = csv_processor.recursive_filters(columns, values)
print(recursive_df)
