from pydantic import BaseModel


class CafeCreate(BaseModel):
    Name: str


class Cafe(CafeCreate):
    Id: int


class Config:
    orm_mode = True

