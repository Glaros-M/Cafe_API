from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/cafes",
    tags=["cafes"]
)


@router.post("")
def create_cafe(cafe: schemas.CafeCreate, db: Session = Depends(get_db)):
    db_cafe = models.Cafes(Name=cafe.Name)
    db.add(db_cafe)
    db.commit()
    db.refresh(db_cafe)
    return db_cafe


@router.get("")
def get_all_cafes(db: Session = Depends(get_db)):
    db_cafes = db.query(models.Cafes).all()
    return db_cafes


@router.put("/{cafe_id}")
def update_cafe(cafe_id: int, cafe: schemas.CafeCreate, db: Session = Depends(get_db)):
    ans = db.query(models.Cafes).filter_by(Id=cafe_id).update(cafe.dict())
    db.commit()
    db_cafe = db.query(models.Cafes).filter_by(Id=cafe_id).first()
    return db_cafe


@router.delete("/{cafe_id}")
def delete_cafe(cafe_id: int,  db: Session = Depends(get_db)):
    db_cafe = db.get(models.Cafes, cafe_id)
    if not db_cafe:
        raise HTTPException(status_code=404, detail="Cafe not found")
    db.delete(db_cafe)
    return {"ok": True}
