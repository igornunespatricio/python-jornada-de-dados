"""Run etl functions."""

from etl import filter_delivered_products, read_csv, sum_prices

path_file = "classes_6_10/project_class_07/vendas.csv"
products = read_csv(path_file)
delivered_products = filter_delivered_products(products)
total = sum_prices(delivered_products)
print(total)
