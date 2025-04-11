from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")

os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/users")
def get_users():
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    return {"data": users}

@app.post("/users")
def add_user(user: User):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    users.append(user.dict())
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)
    return {"message": "User added successfully"}
