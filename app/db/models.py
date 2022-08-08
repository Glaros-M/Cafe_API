from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence, Float
from sqlalchemy.orm import relationship
from .database import Base

"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True )
    name = Column(String, index=True)
    items = relationship("Item", secondary="useritems", back_populates="users")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    users = relationship("User", secondary="useritems", back_populates="items")


class User_Items(Base):
    __tablename__ = "useritems"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
"""


class Cafes(Base):
    __Tablename__ = "Cafes"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)


class Users(Base):
    __Tablename__ = "Users"
    Id = Column(Integer, primary_key=True, index=True)
    Login = Column(String, nullable=False)
    HashedPassword = Column(String, nullable=False)
    Name = Column(String, nullable=False)
    Surname = Column(String, nullable=False)
    Patronymic = Column(String, nullable=False)
    Birthday = Column(String, nullable=False)
    Type = Column(String, nullable=False) # Тут по идее должен быть enum c работник либо клиент


class Employees(Base):
    __Tablename__ = "Employees"
    Id = Column(Integer, primary_key=True, index=True)
    CafeId = Column(Integer,  ForeignKey("Cafes.Id"), nullable=False)
    Login = Column(String, nullable=False)
    HashedPassword = Column(String, nullable=False)
    Name = Column(String, nullable=False)
    Surname = Column(String, nullable=False)
    Patronymic = Column(String, nullable=False)
    Birthday = Column(String, nullable=False)
    Post = Column(String, nullable=False)


class Recipes(Base):
    __Tablename__ = "Recipes"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Description = Column(String, nullable=True)


class RecipeIngredients(Base):
    __Tablename__ = "RecipeIngredients"
    Id = Column(Integer, primary_key=True, index=True)
    RecipeId = Column(Integer,  ForeignKey("Recipes.Id"), nullable=False)
    FoodProductId = Column(Integer,  ForeignKey("FoodProducts.Id"), nullable=False)
    Number = Column(Integer, nullable=False)


class FoodProducts(Base):
    __Tablename__ = "FoodProducts"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)


class Storage(Base):
    __Tablename__ = "Storage"
    Id = Column(Integer, primary_key=True, index=True)
    CafeId = Column(Integer,  ForeignKey("Cafes.Id"), nullable=False)
    FoodProductId = Column(Integer,  ForeignKey("FoodProducts.Id"), nullable=False)
    Measure = Column(String, nullable=False)
    Number = Column(Float, nullable=False)



class Orders(Base):
    __Tablename__ = "Orders"
    Id = Column(Integer, primary_key=True, index=True)
    CafeId = Column(Integer,  ForeignKey("Cafes.Id"), nullable=False)
    UserId = Column(Integer,  ForeignKey("Users.Id"), nullable=False)
    Description = Column(String, nullable=True)


class OrderItems(Base):
    __Tablename__ = "OrderItems"
    Id = Column(Integer, primary_key=True, index=True)
    OrderId = Column(Integer, ForeignKey("Orders.Id"), nullable=False)
    RecipeId = Column(Integer, ForeignKey("Recipes.Id"), nullable=False)


class Feedbacks(Base):
    __Tablename__ = "Feedbacks"
    Id = Column(Integer, primary_key=True, index=True)
    UserId = Column(Integer, ForeignKey("Users.Id"), nullable=False)
    Description = Column(String, nullable=True)
    Grade = Column(Integer, nullable=True)
