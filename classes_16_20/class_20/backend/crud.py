from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel


def get_product(db: Session, product_id: int):
    """
    Returns a product by its id.

    Args:
        db (Session): a session to the database
        product_id (int): the id of the product to retrieve

    Returns:
        ProductModel: the product with the given id, or None if it doesn't exist
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session):
    """
    funcao que retorna todos os elementos
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    """
    Creates a new product in the database.

    Args:
        db (Session): a session to the database
        product (ProductCreate): the product to be created

    Returns:
        ProductModel: the newly created product
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    """
    Deletes a product by its id.

    Args:
        db (Session): a session to the database
        product_id (int): the id of the product to delete

    Returns:
        ProductModel: the deleted product, or None if it doesn't exist
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Updates a product by its id.

    Args:
        db (Session): a session to the database
        product_id (int): the id of the product to update
        product (ProductUpdate): the product to update with

    Returns:
        ProductModel: the updated product, or None if it doesn't exist
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product
