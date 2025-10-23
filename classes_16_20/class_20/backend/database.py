from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Cria o motor do banco de dados, é o conecta com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados, é quem vai executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()


def get_db():
    """
    Generator yielding database sessions.

    Database sessions are used to interact with the database,
    and are the interface to the underlying database engine.

    This function uses a context manager to ensure that the database
    session is properly closed after it is no longer needed.

    The function yields a database session object, which can be used as a context manager.
    This allows the user to use the "with" statement to ensure that the database session is properly closed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
