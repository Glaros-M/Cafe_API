from fastapi import APIRouter
from ..db import schemas
from ..db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.crud import FeedbackCRUD as CRUD


router = APIRouter(
    prefix="/feedbacks",
    tags=["feedbacks"]
)



@router.post("")
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return CRUD.create(feedback, db)


@router.get("")
def get_all_feedbacks(db: Session = Depends(get_db)):
    return CRUD.read_all(db)


@router.get("/{feedback_id}")
def get_one_feedback(feedback_id: int, db: Session = Depends(get_db)):
    return CRUD.read_one(feedback_id, db)


@router.put("/{feedback_id}")
def update_feedback(feedback_id: int, feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return CRUD.update(feedback_id, feedback, db)


@router.delete("/{feedback_id}")
def delete_feedback(feedback_id: int,  db: Session = Depends(get_db)):
    return CRUD.delete(feedback_id, db)
