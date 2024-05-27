from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
  return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
  return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
  db_user = models.User(email=user.email, username=user.username)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


def update_user(db: Session, db_user: models.User, user: schemas.UserBase):
  db_user.username = user.username
  db_user.email = user.email
  db.commit()
  db.refresh(db_user)
  return db_user


def delete_user(db: Session, db_user: models.User):
  db.delete(db_user)
  db.commit()
  return
