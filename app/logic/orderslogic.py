
from ..db import models, schemas
from ..db.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..db import crud


def add_item_to_order(item: schemas.OrderItemsCreate, order_id: int, db: Session):
    item_to_create = schemas.OrderItemsCreate2(**item.dict(), OrderId=order_id)

    # Проверяем есть ли такой рецепт
    #item_to_create.OrderId
    #item_to_create.RecipeId
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
        

    #raise HTTPException(status_code=404, detail=f"{} not found")



    ret = crud.OrderItemsCRUD.create(item_to_create, db)
    return ret


