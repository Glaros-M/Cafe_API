from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str


class UserBase(BaseModel):
    name: str


class UserFromDb(UserBase):
    id: int
    name: str


class ItemCreate(ItemBase):
    owners: list[UserFromDb] = []


class Item(ItemCreate):
    id: int


class User(UserFromDb):
    items: list[ItemBase] = []


class Config:
    orm_mode = True

