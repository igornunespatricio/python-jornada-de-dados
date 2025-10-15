import csv


def read_csv(file_name: str) -> list[dict]:
    """read file and return list of dict"""
    with open(file_name, encoding="utf-8") as file:
        return list(csv.DictReader(file, delimiter=","))


def filter_delivered_products(list_of_products: list[dict]) -> list[dict]:
    delivered_products = []
    for product in list_of_products:
        if product.get("delivery") == "True":
            delivered_products.append(product)

    return delivered_products


def sum_prices(list_of_products: list[dict]) -> float:
    total = 0
    for product in list_of_products:
        total += float(product.get("price"))
    return total
