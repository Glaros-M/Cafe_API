from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence, Float
from sqlalchemy.orm import relationship
from .database import Base


class Cafes(Base):
    __tablename__ = "Cafes"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)


class Users(Base):
    __tablename__ = "Users"
    Id = Column(Integer, primary_key=True, index=True)
    Login = Column(String, nullable=False)
    HashedPassword = Column(String, nullable=False)
    Name = Column(String, nullable=False)
    Surname = Column(String, nullable=False)
    Patronymic = Column(String, nullable=False)
    Birthday = Column(String, nullable=False)
    Type = Column(String, nullable=False) # Тут по идее должен быть enum c работник либо клиент


class Employees(Base):
    __tablename__ = "Employees"
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
    __tablename__ = "Recipes"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)
    Description = Column(String, nullable=True)
    Ingredients = relationship("RecipeIngredients", back_populates='Recipe')


class RecipeIngredients(Base):
    __tablename__ = "RecipeIngredients"
    Id = Column(Integer, primary_key=True, index=True)
    RecipeId = Column(Integer,  ForeignKey("Recipes.Id"), nullable=False)
    FoodProductId = Column(Integer,  ForeignKey("FoodProducts.Id"), nullable=False)
    Number = Column(Float, nullable=False)
    Recipe = relationship("Recipes", back_populates='Ingredients')


class FoodProducts(Base):
    __tablename__ = "FoodProducts"
    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, nullable=False)


class Storage(Base):
    __tablename__ = "Storage"
    Id = Column(Integer, primary_key=True, index=True)
    CafeId = Column(Integer,  ForeignKey("Cafes.Id"), nullable=False)
    FoodProductId = Column(Integer,  ForeignKey("FoodProducts.Id"), nullable=False)
    Measure = Column(String, nullable=False)
    Number = Column(Float, nullable=False)


class Orders(Base):
    __tablename__ = "Orders"
    Id = Column(Integer, primary_key=True, index=True)
    CafeId = Column(Integer,  ForeignKey("Cafes.Id"), nullable=False)
    UserId = Column(Integer,  ForeignKey("Users.Id"), nullable=False)
    Description = Column(String, nullable=True)
    #Items = relationship("Recipes", secondary="OrderItems", back_populates="items")
    #Разобраться и вставить связи


class OrderItems(Base):
    __tablename__ = "OrderItems"
    Id = Column(Integer, primary_key=True, index=True)
    OrderId = Column(Integer, ForeignKey("Orders.Id"), nullable=False)
    RecipeId = Column(Integer, ForeignKey("Recipes.Id"), nullable=False)


class Feedbacks(Base):
    __tablename__ = "Feedbacks"
    Id = Column(Integer, primary_key=True, index=True)
    UserId = Column(Integer, ForeignKey("Users.Id"), nullable=False)
    Description = Column(String, nullable=True)
    Grade = Column(Integer, nullable=True)
