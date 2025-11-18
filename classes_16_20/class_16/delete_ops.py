from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text


# Supondo que o banco de dados seja SQLite e esteja no arquivo `database.db`
engine = create_engine("sqlite:///classes_16_20/class_16/database.db")

# Criação da sessão
with Session(engine) as session:
    # Sua consulta SQL
    statement = text("DROP TABLE hero;")

    # Executando a consulta
    results = session.exec(statement)
