from typing import Dict, Union, Optional, Any, List
import json

# TYPE HINT

# age: int = 30
# height: float = 1.70
# name: str = 'Igor'
# is_active: bool = True

# age = 'hello'

# LISTS
# products = ['shoes', 't-shirt', 'videogame']
# new_product = "ball"
# products.append(new_product)
# print(products)
# products.pop()
# products.pop()
# products.remove('shoes')
# new_products = ['glasses', 'plate']
# products.extend(new_products)
# for item in ['item1', 0]:
#     print(type(item))

# DICTIONARY

# d: dict = {
#     "string": 'hello world',
#     "number": 5,
#     "list": [1, 'string', True]
# }

# d2: dict = {
#     "item1": 0,
#     "hello": [1, 3, 5],
#     "etc": True
# }

# final: list = []
# final.append(d)
# final.append(d2)

# final_json = json.dumps(final, indent=4,)
# print(final_json)

# dictionary: Dict[str, Union[int, str, float]] = {}

# dictionary

# data structure with year, title and author of publication
book1: Dict[str, Any] = {
    "Title": "Title of book",
    "Author": "Author of publication",
    "Year": "Year of publication",
}

book2: Dict[str, Any] = {
    "Title": "Title of book 2",
    "Author": "Author of publication 2",
    "Year": "Year of publication 2",
}


books: Dict[str, dict] = {}
books["book 1"] = book1
books["book 2"] = book2
print(books)
print('finished code')

