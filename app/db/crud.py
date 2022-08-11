from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


class BaseCRUD:
    def __init__(self, name, model, schema):
        """Можно добавить сюда схема создания, схема полная что бы указывать responce_model"""
        self.name = name
        self.model = model
        self.schema = schema

    def create(self, data, db: Session):
        db_item = self.model(**data.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def read_all(self, db: Session):
        db_item = db.query(self.model).all()
        return db_item

    def read_one(self, id: int, db: Session):
        db_item = db.get(self.model, id)
        return db_item

    def update(self, id: int, item,  db: Session):
        ans = db.query(self.model).filter_by(Id=id).update(item.dict())
        db.commit()
        db_item = db.query(self.model).filter_by(Id=id).first()
        return db_item

    def delete(self, id: int, db: Session):
        db_item = db.get(self.model, id)
        if not db_item:
            raise HTTPException(status_code=404, detail=f"{self.name} not found")
        db.delete(db_item)
        db.commit()
        return {"ok": True}


CafeCRUD = BaseCRUD("Cafe", models.Cafes, schemas.CafeCreate)
EmploeeCRUD = BaseCRUD("Employee", models.Employees, schemas.EmploeeCreate)
FeedbackCRUD = BaseCRUD("Feedback", models.Feedbacks, schemas.FeedbackCreate)
StorageCRUD = BaseCRUD("Storage", models.Storage, schemas.StorageCreate)
OrdersCRUD = BaseCRUD("Order", models.Orders, schemas.OrdersCreate)
OrderItemsCRUD = BaseCRUD("OrderItem", models.OrderItems, schemas.OrderItemsCreate)
FoodProductsCRUD = BaseCRUD("FoodProduct", models.FoodProducts, schemas.FoodProductsCreate)
