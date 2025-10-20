from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random


app = FastAPI(debug=True)
fake = Faker()


@app.get("/")
async def hello_world():
    return "Coca-Cola me patrocina!"


@app.get("/gerar_compra")
async def gerar_compra():
    return [
        {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": fake.word().title() + " " + fake.word().title(),
            "ean": fake.random_int(min=1000, max=9999),
            "price": fake.pydecimal(left_digits=3, right_digits=2, positive=True),
            "clientPosition": fake.location_on_land(),
            "store": fake.random_int(min=1, max=10),
            "dateTime": fake.iso8601(),
        }
    ]


@app.get("/gerar_compras/{numero_registro}")
async def gerar_compra(numero_registro: int):

    if numero_registro < 1:
        return {"error": "O número deve ser maior que 1"}

    respostas = []
    for _ in range(numero_registro):
        try:
            compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": fake.word().title() + " " + fake.word().title(),
                "ean": fake.random_int(min=1000, max=9999),
                "price": fake.pydecimal(left_digits=3, right_digits=2, positive=True),
                "clientPosition": fake.location_on_land(),
                "store": fake.random_int(min=1, max=10),
                "dateTime": fake.iso8601(),
            }
            respostas.append(compra)
        except IndexError as e:
            print(f"Erro de índice: {e}")
        except ValueError as e:
            print(f"Erro inesperado: {e}")
            compra = {
                "client": fake.name(),
                "creditcard": fake.credit_card_provider(),
                "product": "error",
                "ean": 0,
                "price": 0.0,
                "clientPosition": fake.location_on_land(),
                "store": fake.random_int(min=1, max=10),
                "dateTime": fake.iso8601(),
            }
            respostas.append(compra)
        except Exception as e:
            print(f"Erro inesperado: {e}")
    return respostas
