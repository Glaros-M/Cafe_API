from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/food-products",
    tags=["food-products"]
)


@router.post("")
def create_product(product: schemas.FoodProductsCreate, db: Session = Depends(get_db)):
    db_product = models.FoodProducts(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(models.FoodProducts).all()
    return db_products


@router.put("/{product_id}")
def update_product(product_id: int, product: schemas.FoodProductsCreate, db: Session = Depends(get_db)):
    ans = db.query(models.FoodProducts).filter_by(Id=product_id).update(product.dict())
    db.commit()
    db_recipe = db.query(models.FoodProducts).filter_by(Id=product_id).first()
    return db_recipe


@router.delete("/{product_id}")
def delete_product(product_id: int,  db: Session = Depends(get_db)):
    db_product = db.get(models.FoodProducts, product_id)
    if not db_product:
        # вынести в отдельную функцию проверки существования
        raise HTTPException(status_code=404, detail="Food product not found")
    db.delete(db_product)
    db.commit()
    return {"ok": True}

