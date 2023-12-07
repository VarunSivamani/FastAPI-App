import os
from dotenv import load_dotenv

from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth

load_dotenv()

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

while True:   
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', 
            password=os.getenv("DB_PASSWORD"), cursor_factory=RealDictCursor
        )

        cursor = conn.cursor()
        print("Database connection was successfull")
        break

    except Exception as error:
        print("Connection failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [
    {
        "title": "Title Post-1",
        "content": "Content Post-1",
        "id": 1
    },
    {
        "title": "Fav foods",
        "content": "I like Pizza",
        "id": 2
    }
] 

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
        

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message":"hi"}