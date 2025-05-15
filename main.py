from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 allow your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    author: str
    timestamp: datetime

# In-memory "database"
blog_posts = []

# Create a blog post
@app.post("/posts/")
def create_post(post: BlogPost):
    blog_posts.append(post)
    return {"message": "Post created successfully!"}

# Get all posts
@app.get("/posts/", response_model=List[BlogPost])
def get_posts():
    return blog_posts

# Get a single post by id
@app.get("/posts/{post_id}", response_model=BlogPost)
def get_post(post_id: int):
    for post in blog_posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

# Update a post by id
@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: BlogPost):
    for index, post in enumerate(blog_posts):
        if post.id == post_id:
            blog_posts[index] = updated_post
            return {"message": "Post updated successfully!"}
    raise HTTPException(status_code=404, detail="Post not found")

# Delete a post by id
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for index, post in enumerate(blog_posts):
        if post.id == post_id:
            blog_posts.pop(index)
            return {"message": "Post deleted successfully!"}
    raise HTTPException(status_code=404, detail="Post not found")
