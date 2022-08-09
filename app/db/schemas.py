from pydantic import BaseModel


class CafeCreate(BaseModel):
    Name: str


class Cafe(CafeCreate):
    Id: int


class UserCreate(BaseModel):
    """Some text about UserCreate"""
    Login: str
    Password: str
    Name: str
    Surname: str
    Patronymic: str
    Birthday: str
    Type: str


class User(UserCreate):
    Id: int


class RecipeCreate(BaseModel):
    Name: str
    Description: str


class Recipe(RecipeCreate):
    Id: int
    Ingredients: list["RecipeIngredients"]


class RecipeIngredientsCreate(BaseModel):
    FoodProductId: int
    Number: float


class RecipeIngredients(RecipeIngredientsCreate):
    Id: int
    RecipeId: int


class RecipePrint(BaseModel):
    recipe: Recipe
    ingredients: list[RecipeIngredients]


class FoodProductsCreate(BaseModel):
    Name: str


class FoodProducts(FoodProductsCreate):
    Id: int

class Config:
    orm_mode = True


