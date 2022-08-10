from pydantic import BaseModel


class CafeCreate(BaseModel):
    Name: str


class Cafe(CafeCreate):
    Id: int


class UserBase(BaseModel):
    Login: str
    Name: str
    Surname: str
    Patronymic: str
    Birthday: str
    Type: str


class UserCreate(UserBase):
    """Some text about UserCreate"""
    Password: str

class UserToDB(UserBase):
    HashedPassword: str


class User(UserBase):
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


class EmployeeBase(BaseModel):
    CafeId: int
    Login: str
    Name: str
    Surname: str
    Patronymic: str
    Birthday: str
    Post: str


class EmploeeCreate(EmployeeBase):
    Password: str


class EmploeeToDB(EmployeeBase):
    HashedPassword: str


class Employee(EmployeeBase):
    Id: int


class FeedbackCreate(BaseModel):
    UserId: int
    Description: str
    Grade: int


class Feedback(FeedbackCreate):
    Id: int


class StorageCreate(BaseModel):
    CafeId: int
    FoodProductId: int
    Measure: str
    Number: int


class Storage(StorageCreate):
    Id: int


class OrdersCreate(BaseModel):
    CafeId: int
    UserId: int
    Description: str


class Orders(OrdersCreate):
    Id: int


class OrderItemsCreate(BaseModel):
    OrderId: int
    RecipeId: int


class OrderItems(OrderItemsCreate):
    Id: int


class Config:
    orm_mode = True


