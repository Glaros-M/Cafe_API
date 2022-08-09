from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/recipes",
    tags=["recipes"]
)


@router.post("")
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = models.Recipes(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


# response_model=list[schemas.RecipePrint]
@router.get("")
def get_all_recipes(db: Session = Depends(get_db)):
    db_recipes = db.query(models.Recipes).all()
    ans = []
    for rec in db_recipes:
        db_ingresients = db.query(models.RecipeIngredients).filter_by(RecipeId=rec.Id).all()
        """db_ingresients = db_ingresients.join(models.RecipeIngredients.FoodProductId, models.RecipeIngredients.FoodProductId == models.FoodProducts.Id)
        db_ingresients = db_ingresients.all()"""
        for ingredient in db_ingresients:
            product = db.get(models.FoodProducts, ingredient.FoodProductId)
            ingredient.__dict__.update({"ProductName": product.Name})
        ans.append({"recipe": rec, "ingredients": db_ingresients})
    return ans




@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    ans = db.query(models.Recipes).filter_by(Id=recipe_id).update(recipe.dict())
    db.commit()
    db_recipe = db.query(models.Recipes).filter_by(Id=recipe_id).first()
    return db_recipe


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int,  db: Session = Depends(get_db)):
    db_recipe = db.get(models.Recipes, recipe_id)
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(db_recipe)
    db.commit()
    return {"ok": True}

