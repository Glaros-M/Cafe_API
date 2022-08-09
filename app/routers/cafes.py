from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session
from ..db.crud import CafeCRUD


router = APIRouter(
    prefix="/cafes",
    tags=["cafes"]
)


@router.post("")
def create_cafe(cafe: schemas.CafeCreate, db: Session = Depends(get_db)):
    return CafeCRUD.create(cafe, db)


@router.get("")
def get_all_cafes(db: Session = Depends(get_db)):
    return CafeCRUD.read_all(db)


@router.get("/{cafe_id}")
def get_one_cafe(cafe_id: int, db: Session = Depends(get_db)):
    return CafeCRUD.read_one(cafe_id, db)


@router.put("/{cafe_id}")
def update_cafe(cafe_id: int, cafe: schemas.CafeCreate, db: Session = Depends(get_db)):
    return CafeCRUD.update(cafe_id, cafe, db)


@router.delete("/{cafe_id}")
def delete_cafe(cafe_id: int,  db: Session = Depends(get_db)):
    return CafeCRUD.delete(cafe_id, db)
