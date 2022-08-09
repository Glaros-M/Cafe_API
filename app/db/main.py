import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import update

from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List
from ..routers import cafes, users, recipes, foodproducts, recipeingredients


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(cafes.router)
app.include_router(users.router)
app.include_router(recipes.router)
app.include_router(foodproducts.router)
app.include_router(recipeingredients.router)



