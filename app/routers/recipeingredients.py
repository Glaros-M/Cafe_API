from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/recipes/{recipe_id}",
    tags=["recipes", "ingredients"]
)


@router.post("/ingredients")
def add_ingredient_to_recipe(recipe_id: int, ingredient: schemas.RecipeIngredientsCreate, db: Session = Depends(get_db)):
    db_ingredient = models.RecipeIngredients(**ingredient.dict(), RecipeId=recipe_id)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient


@router.get("/ingredients")
def get_all_ingredients(recipe_id: int, db: Session = Depends(get_db)):
    db_recipes = db.query(models.RecipeIngredients).filter_by(RecipeId=recipe_id).all()
    return db_recipes


@router.put("/ingredients/{ingredient_id}")
def update_ingredient(recipe_id: int, ingredient_id: int, ingredient: schemas.RecipeIngredientsCreate, db: Session = Depends(get_db)):
    ans = db.query(models.RecipeIngredients).filter_by(Id=ingredient_id, RecipeId=recipe_id).update(ingredient.dict())
    db.commit()
    db_recipe = db.query(models.RecipeIngredients).filter_by(Id=ingredient_id, RecipeId=recipe_id).first()
    return db_recipe


@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int,  db: Session = Depends(get_db)):
    db_ingredient = db.get(models.RecipeIngredients, ingredient_id)
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    db.delete(db_ingredient)
    db.commit()
    return {"ok": True}

