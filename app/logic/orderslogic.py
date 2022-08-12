
from ..db import models, schemas
from ..db.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..db import crud


def _check_order_and_recipe(item_to_create: schemas.OrderItemsCreate2, db: Session):
    order: schemas.Orders = crud.OrdersCRUD.read_one(item_to_create.OrderId, db)
    recipe: schemas.Recipe = db.get(models.Recipes, item_to_create.RecipeId)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order not found")
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Recipe not found")


def add_item_to_order(item: schemas.OrderItemsCreate, order_id: int, db: Session):
    item_to_create = schemas.OrderItemsCreate2(**item.dict(), OrderId=order_id)

    _check_order_and_recipe(item_to_create, db)

    order: schemas.Orders = crud.OrdersCRUD.read_one(item_to_create.OrderId, db)
    recipe: schemas.Recipe = db.get(models.Recipes, item_to_create.RecipeId)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order not found")
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Recipe not found")

    ingredients: list[schemas.RecipeIngredients]
    ingredients = db.query(models.RecipeIngredients).filter_by(RecipeId=recipe.Id).all()

    for ingredient in ingredients:

        foodproduct: schemas.FoodProducts = db.get(models.FoodProducts, ingredient.FoodProductId)
        stored_food_product = db.query(models.Storage).\
            filter_by(CafeId=order.CafeId, FoodProductId=ingredient.FoodProductId).first()
        if not stored_food_product:
            raise HTTPException(status_code=404, detail=f"Отсутствует документация склада по {foodproduct.Name}")



        if ingredient.Number > stored_food_product.Number:
            raise HTTPException(status_code=422, detail=f"На складе недостаточно {foodproduct.Name}")

        stored_food_product.Number = stored_food_product.Number - ingredient.Number

        a = db.query(models.Storage).filter_by(Id=stored_food_product.Id)#.update(stored_food_product)
        a.update({"Number": stored_food_product.Number})

        db.commit()


    ret = crud.OrderItemsCRUD.create(item_to_create, db)
    return ret

