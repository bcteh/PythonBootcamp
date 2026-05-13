# use mongo fastapi
# use uvicorn file_name:app  to run the server. e.g. uvicorn 17_fastsql:app --reload

import os
import sys
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime   
from dotenv import load_dotenv
from xmlrpc import client
from pymongo import MongoClient


load_dotenv()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("18_fastapimongo18:app", host="0.0.0.0", port=8000)

# connect to mongo db
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
users_collection = db["users"]

app = FastAPI()

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
    model_config = ConfigDict(extra='ignore')
    loginid: str
    name: str
    age: int
    email: EmailStr
    created_at: datetime
class PostResponse(BaseModel):
    message: str
class PostResponseForUserNotFound(BaseModel):
    message: str

@app.on_event("startup")
async def startup_event():
    global client, db, users_collection
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command('ping')
        db = client["mydatabase"]
        users_collection = db["users"]
    except Exception as e:
        raise Exception(f"Failed to connect to MongoDB at {MONGO_URI}. Error: {str(e)}")

@app.on_event("shutdown")
async def shutdown_event():
    if client:
        client.close()

@app.get("/")
def root():
    return {"message": "Welcome to Mongo DB API", "docs": "/docs"}

# Create a post endpoint to create a user based on loginid.
@app.post("/users/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    try:
        user_data = user.model_dump()
        user_data["created_at"] = datetime.now()
        users_collection.insert_one(user_data)
        return PostResponse(message=f"User with loginid '{user.loginid}' created.")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error creating user: {str(e)}")

# Create a get endpoint to get all users.
@app.get("/users/", response_model=List[UserResponse])
def get_all_users():
    if users_collection is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database connection not initialized.")
    try:
        users = list(users_collection.find())
        if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found.")
        return users
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error occurred while fetching users: {str(e)}")
# Create a get endpoint to get a user by loginid.
@app.get("/users/{loginid}", response_model=UserResponse)
def get_user(loginid: str):
    user = users_collection.find_one({"loginid": loginid})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with loginid '{loginid}' not found.")
    return user

# Create a delete endpoint to delete a user based on loginid.
@app.delete("/users/{loginid}", response_model=PostResponse)
def delete_user(loginid: str):
    try:
        users_collection.delete_one({"loginid": loginid})
        return PostResponse(message=f"User with loginid '{loginid}' deleted.")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
# Create a put endpoint to update a user based on loginid, if user does not exist, return no user found. 
@app.put("/users/{loginid}", response_model=PostResponse)
def update_user(loginid: str, user_update: UserUpdate):
    try:
        result = users_collection.update_one(
            {"loginid": loginid},
            {"$set": user_update.model_dump(exclude_unset=True)},
            upsert=True
            )
        return PostResponse(message=f"User with loginid '{loginid}' updated or inserted.")  
    except Exception as e:
            if result.matched_count == 0:
                return PostResponseForUserNotFound(message=f"User with loginid '{loginid}' not found. No update performed.")
