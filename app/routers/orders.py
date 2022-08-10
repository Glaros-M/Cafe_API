from fastapi import APIRouter
from ..db import schemas
from ..db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.crud import OrdersCRUD as CRUD


router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post("")
def create_order(order: schemas.OrdersCreate, db: Session = Depends(get_db)):
    return CRUD.create(order, db)


@router.get("")
def get_all_orders(db: Session = Depends(get_db)):
    return CRUD.read_all(db)


@router.get("/{order_id}")
def get_one_order(order_id: int, db: Session = Depends(get_db)):
    return CRUD.read_one(order_id, db)


@router.put("/{order_id}")
def update_order(order_id: int, order: schemas.OrdersCreate, db: Session = Depends(get_db)):
    return CRUD.update(order_id, order, db)


@router.delete("/{order_id}")
def delete_order(order_id: int,  db: Session = Depends(get_db)):
    return CRUD.delete(order_id, db)
