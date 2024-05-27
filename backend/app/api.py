from fastapi import APIRouter

from app.routes import users
from . import models
from .db import engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()
router.include_router(users.router, prefix="/users")
