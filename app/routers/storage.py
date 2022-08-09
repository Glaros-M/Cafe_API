from fastapi import APIRouter
from ..db import schemas
from ..db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.crud import StorageCRUD as CRUD


router = APIRouter(
    prefix="/storage",
    tags=["storage"]
)

"""
Надо еще раз внимательно продумать таблицу. 
Возможно обязательно необходим составной ключ для этой и похожей таблицы.

"""


@router.post("")
def add_product_to_storage(storage: schemas.StorageCreate, db: Session = Depends(get_db)):
    return CRUD.create(storage, db)


@router.get("")
def get_all_products_from_storage(db: Session = Depends(get_db)):
    return CRUD.read_all(db)


@router.get("/{storage_id}")
def get_one_stored_product(storage_id: int, db: Session = Depends(get_db)):
    return CRUD.read_one(storage_id, db)


@router.put("/{storage_id}")
def update_storage(storage_id: int, storage: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return CRUD.update(storage_id, storage, db)


@router.delete("/{storage_id}")
def delete_product_from_storage(storage_id: int,  db: Session = Depends(get_db)):
    return CRUD.delete(storage_id, db)
