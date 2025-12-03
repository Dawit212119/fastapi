
from fastapi import FastAPI,HTTPException
from app.schema import PostCreate
app=FastAPI()
text_posts ={
1: {"title": "New Post", "content": "Cool test post"},
2: {"title": "Python Tip", "content": "Use list comprehensions for cleaner loops."},
3: {"title": "Daily Motivation", "content": "Consistency beats intensity every time."},
4: {"title": "Fun Fact", "content": "The first computer bug was an actual moth found in a Harvard Mark II."},
5: {"title": "Update", "content": "Just launched my new project! Excited to share more soon."},
6: {"title": "Tech Insight", "content": "Async I0 in Python can massively speed up I/0-bound tasks."},
7: {"title": "Quote", "content": "Programs must be written for people to read, and only incidentally for machi"},
8: {"title": "Weekend Plans", "content": "Might finally clean up my GitHub repos ... or just play some Minecraft"},
9: {"title": "Question", "content": "What's the most underrated Python library you've ever used?"},
10: {"title": "Mini Announcement", "content": "New video drops tomorrow-covering the weirdest Python features!"}
}

@app.get("/hello")
def  hello ():
   return {"message":"hello world"}   # dict =>  json


@app.get("/posts")
def get_all_posts(limit:int = None):  # query parameter
   if limit:
      return list(text_posts.values())[:limit] #  conver dict to list then slice 
   return text_posts

@app.get("/posts/{id}")   #  path parameter  
def getPostById(id:int):
   if id not in text_posts:
      raise HTTPException(status_code=404,detail="post not found")  # throw an error  
   return text_posts[id]

@app.post("/post")
def create_post(post:PostCreate) -> PostCreate:
   newPost={"title":post.title,"content":post.content}
   text_posts[max(text_posts.keys())+1]=newPost

   return newPost
@app.delete("/deletepost/{id}")
def delete_post(id:int):
   if  id not in text_posts:
      raise HTTPException(status_code=404,detail="post with this id is not exist")
   text_posts.pop(id)
   return  text_posts
   
   
