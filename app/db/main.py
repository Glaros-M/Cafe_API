import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session, joinedload

from . import crud, models, schemas
from .database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/users")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    db_books = db.query(models.User).options(joinedload(models.User.items)).all()
    return db_books


@app.post("/items")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(title=item.title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    add_owners(db_item.id, item.owners, db)
    db.refresh(db_item)
    return db_item


def add_owners(item_id: int, owners: List[schemas.UserFromDb], db: Session = Depends(get_db)):
    list1 = []
    for owner in owners:
        db_useritems = models.User_Items(user_id=owner.id, item_id=item_id)
        db.add(db_useritems)
        db.commit()
        list1.append(db_useritems)
    return list1


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



