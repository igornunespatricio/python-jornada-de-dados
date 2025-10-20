# ORM

Object Relational Maping - abstracts communication with database

# SQLModel

Uses SQLAlchemy to speak with database and use pydantic for data quality. No need to develop CRUD code, they are implemented in methods.

SQLAlchemy can speak various dialects: Microsoft SQL Server, My SQL, MariaDB, Oracle, PostgreSQL, SQLite, Big Query, IBM, Google Sheets, SAP, Snowflake, Duckdb and much more.

SQLModel deals with SQL Injection problem

tiangolo: fastapi, SQLModel and Pydantic

# SQLAlchemy

Decouple SQL model from other codes such as database, views, controllers, etc.

Write data model, don't need to write SQL queries, abstract DB.

MVC pattern - model-view-controller.

DBAPI - python database api documentation - patterns of database communication

Pool - database has connection limits - you can limit the number of connections to the database

ORM: each class is a table in the database, each object is a row in the database and each attribute is a column in a table in the database. Code below is used for that.

```python
Base = declarative_base()
```
