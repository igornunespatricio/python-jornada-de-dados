from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()


@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Creates a new product in the database.

    Args:
        product (ProductCreate): The product to be created
        db (Session): A session to the database

    Returns:
        ProductResponse: The newly created product
    """
    return create_product(db=db, product=product)


@router.get("/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    """
    Retrieves all products from the database.

    Args:
        db (Session): A session to the database

    Returns:
        List[ProductResponse]: A list of all products
    """
    products = get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a product by its id from the database.

    Args:
        product_id (int): The id of the product to retrieve
        db (Session): A session to the database

    Returns:
        ProductResponse: The retrieved product

    Raises:
        HTTPException: If the product with the given id doesn't exist
    """
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}", response_model=ProductResponse)
def detele_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Deletes a product by its id from the database.

    Args:
        product_id (int): The id of the product to delete
        db (Session): A session to the database

    Returns:
        ProductResponse: The deleted product

    Raises:
        HTTPException: If the product with the given id doesn't exist
    """
    db_product = delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    """
    Updates a product by its id.

    Args:
        product_id (int): The id of the product to update
        product (ProductUpdate): The product to update with
        db (Session): A session to the database

    Returns:
        ProductResponse: The updated product

    Raises:
        HTTPException: If the product with the given id doesn't exist
    """
    db_product = update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
