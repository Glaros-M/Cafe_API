from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemBase, user_ids: list[int]):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    for id in user_ids:
        _create_user_item(db, id, db_item.id)
    return db_item


def _create_user_item(db: Session, user_id: int, item_id: int):
    db_user_item = models.User_Items(user_id=user_id, item_id=item_id)
    db.add(db_user_item)
    db.commit()
    db.refresh(db_user_item)
    return db_user_item
