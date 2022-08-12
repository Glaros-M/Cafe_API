from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.crud import OrderItemsCRUD as CRUD
from ..logic import orderslogic

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post("/{order_id}/items")
def add_item_to_order(order_id: int, item: schemas.OrderItemsCreate, db: Session = Depends(get_db)):
    #db_item = schemas.OrderItemsCreate2(**item.dict(), OrderId=order_id)
    db_item = orderslogic.add_item_to_order(item, order_id, db)
    return db_item


@router.get("/{order_id}/items")
def get_all_items(order_id: int, db: Session = Depends(get_db)):
    db_items = db.query(models.OrderItems).filter_by(OrderId=order_id).all()
    return db_items


@router.put("/{order_id}/items/{item_id}")
def update_ingredient(order_id: int, item_id: int, item: schemas.OrderItems, db: Session = Depends(get_db)):
    """Надо продумать до конца. Возможно поменять структуру. т.к. сейчас можно поменять orderID и
    вернется или NULL или не те данные"""
    ans = db.query(models.OrderItems).filter_by(Id=item_id, OrderId=order_id).update(item.dict())
    db.commit()
    db_item = db.query(models.OrderItems).filter_by(Id=item_id, OrderId=order_id).first()
    return db_item


@router.delete("/{order_id}/items/{item_id}")
def delete_ingredient(item_id: int,  db: Session = Depends(get_db)):
    return CRUD.delete(item_id, db)

