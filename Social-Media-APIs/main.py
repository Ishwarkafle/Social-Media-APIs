from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool =True
    rating : Optional[int]=None
    
@app.get("/")
async def root():
    return {"message": "Welcome to the Social Media API!"}


@app.get("/posts")
async def get_posts():
    return {"data":"Hre are your Social Media Posts!"}


#creating postrequest
#@app.post("/about")

#async def post_post(paylaod: dict = Body(...)):
    print(paylaod)
    
    return {"new_dta":f"title {paylaod['title']} content {paylaod['content']}"}



@app.post("/createpost")
async def create_post(new_post: Post):
    print(new_post.published)
    print(new_post.rating)
    return {"message": f"Post created with title: {new_post.title} and content: {new_post.content}"}
