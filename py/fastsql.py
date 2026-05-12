#fastapi
import os
import sys
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime   
import sqlite3

sys.path.append(os.path.dirname(__file__))
from sql_database import Databasemanager
app = FastAPI()


# Database connection
db_manager = Databasemanager("example.db")


# Pydantic model for user input and response
class User(BaseModel):
    loginid: str
    name: str
    age: int
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None

class UserResponse(BaseModel):
    model_config = {"from_attributes": True}
    loginid: str
    name: str
    age: int
    email: EmailStr
    created_at: datetime

class PostResponse(BaseModel):
    message: str

class PostResponseForUserNotFound(BaseModel):
    message: str


# Create a post endpoint to create a user based on loginid.
@app.post("/users/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    try:
        db_manager.create_user(user.loginid, user.name, user.age, user.email)
        return PostResponse(message=f"User with loginid '{user.loginid}' created.")
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with loginid '{user.loginid}' already exists.")

# Create a get endpoint to get a user by loginid.
@app.get("/users/{loginid}", response_model=UserResponse)
def get_user(loginid: str):
    user = db_manager.get_user_by_loginid(loginid)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with loginid '{loginid}' not found.")
    return user 
# Create a put endpoint to update a user based on loginid.
@app.put("/users/{loginid}", response_model=PostResponse)   
def update_user(loginid: str, user_update: UserUpdate):
    try:
        db_manager.update_user(loginid, user_update.name, user_update.age, user_update.email)
        return PostResponse(message=f"User with loginid '{loginid}' updated.")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))   
# Create a delete endpoint to delete a user based on loginid.
@app.delete("/users/{loginid}", response_model=PostResponse)
def delete_user(loginid: str):
    try:
        db_manager.delete_user(loginid)
        return PostResponse(message=f"User with loginid '{loginid}' deleted.")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))   
# Create a get endpoint to get all users.
@app.get("/users/", response_model=List[UserResponse])
def get_all_users():
    users = db_manager.get_all_users()
    return users
