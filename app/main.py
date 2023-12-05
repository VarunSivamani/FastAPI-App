from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

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

@app.get("/")
async def root():
    return {"hi":"hi"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/createposts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(int(id))

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"Post with id {id} was not found"
        )
    
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find index of the array that has the req id
    # my_post.pop(index)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Post with id {id} does not exist"
        )

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Post with id {id} does not exist"
        )

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict

    return {"data": post_dict}