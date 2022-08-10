import uvicorn
from fastapi import FastAPI

from .db import models
from .db.database import engine
from .routers import cafes, users, recipes, foodproducts, recipeingredients, employees, feedbacks,\
    storage, orders, orderitems


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(cafes.router)
app.include_router(users.router)
app.include_router(recipes.router)
app.include_router(foodproducts.router)
app.include_router(recipeingredients.router)
app.include_router(employees.router)
app.include_router(feedbacks.router)
app.include_router(storage.router)
app.include_router(orders.router)
app.include_router(orderitems.router)

