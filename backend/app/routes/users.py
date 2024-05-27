from fastapi import APIRouter, Depends, HTTPException
from app import schemas, crud
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = crud.get_users(db, skip=skip, limit=limit)
  return users


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
  db_user = crud.get_user_by_username(db, username=user.username)
  if db_user:
    raise HTTPException(status_code=400, detail="Username already registered")
  return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = crud.get_user(db, user_id=user_id)
  print(user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return db_user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserBase, db: Session = Depends(get_db)):
  db_check = crud.get_user_by_username(db, username=user.username)
  if db_check and db_check.id != user_id:
    raise HTTPException(status_code=400, detail="Username already registered")

  db_user = crud.get_user(db, user_id=user_id)

  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  db_user = crud.update_user(db, db_user, user)
  return db_user


@router.delete("/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
  db_user = crud.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  crud.delete_user(db, db_user)
  return db_user
