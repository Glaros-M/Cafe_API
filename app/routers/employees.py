from fastapi import APIRouter
from ..db import schemas
from ..db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.crud import EmploeeCRUD as CRUD


router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)


def fake_hash_password_in_schema_object(data):
    b = schemas.EmploeeToDB(**data.dict(), HashedPassword=data.Password)
    return b


@router.post("")
def create_employee(employee: schemas.EmploeeCreate, db: Session = Depends(get_db)):
    data = fake_hash_password_in_schema_object(employee)
    ans = CRUD.create(data, db)
    data = schemas.Employee(**ans.__dict__)
    return data


@router.get("")
def get_all_employees(db: Session = Depends(get_db)):
    return CRUD.read_all(db)


@router.get("/{employee_id}")
def get_one_employee(employee_id: int, db: Session = Depends(get_db)):
    return CRUD.read_one(employee_id, db)


@router.put("/{employee_id}")
def update_employee(employee_id: int, employee: schemas.EmploeeCreate, db: Session = Depends(get_db)):
    return CRUD.update(employee_id, employee, db)


@router.delete("/{employee_id}")
def delete_employee(employee_id: int,  db: Session = Depends(get_db)):
    return CRUD.delete(employee_id, db)
