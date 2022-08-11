from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session
from ..db.crud import FoodProductsCRUD as CRUD


router = APIRouter(
    prefix="/food-products",
    tags=["food-products"]
)


@router.post("")
def create_product(product: schemas.FoodProductsCreate, db: Session = Depends(get_db)):
    return CRUD.create(product, db)


@router.get("")
def get_all_products(db: Session = Depends(get_db)):
    return CRUD.read_all(db)


@router.put("/{product_id}")
def update_product(product_id: int, product: schemas.FoodProductsCreate, db: Session = Depends(get_db)):
    return CRUD.update(product_id, product, db)


@router.delete("/{product_id}")
def delete_product(product_id: int,  db: Session = Depends(get_db)):
    return CRUD.delete(product_id, db)

