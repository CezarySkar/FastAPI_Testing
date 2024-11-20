from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from utils import set_password, check_password_hash

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code = status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    user_dto = models.User(**user.model_dump())
    user_dto.set_password(user_dto.password)
    db.add(user_dto)
    db.commit()