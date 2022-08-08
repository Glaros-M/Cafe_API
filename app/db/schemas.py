from pydantic import BaseModel


class CafeCreate(BaseModel):
    Name: str


class Cafe(CafeCreate):
    Id: int


class UserCreate(BaseModel):
    Login: str
    HashedPassword: str
    Name: str
    Surname: str
    Patronymic: str
    Birthday: str
    Type: str


class User(UserCreate):
    Id: int


class Config:
    orm_mode = True


