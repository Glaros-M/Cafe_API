from fastapi import APIRouter
from ..db import models, schemas
from ..db.database import get_db
from fastapi import Depends,  HTTPException
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


def fake_hash_password_in_schema_object(data):
    b = schemas.UserToDB(**data.dict(), HashedPassword=data.Password)
    return b


@router.post("")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    data = fake_hash_password_in_schema_object(user)
    db_user = models.Users(**data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db_user = schemas.User(**db_user.__dict__)
    return db_user


@router.get("")
def get_all_users(db: Session = Depends(get_db)):
    db_users = db.query(models.Users).all()
    return db_users


@router.put("/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    ans = db.query(models.Users).filter_by(Id=user_id).update(user.dict())
    db.commit()
    db_user = db.query(models.Users).filter_by(Id=user_id).first()
    return db_user


@router.delete("/{user_id}")
def delete_user(user_id: int,  db: Session = Depends(get_db)):
    db_user = db.get(models.Users, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()

    return {"ok": True}
