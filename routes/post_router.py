from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from validation.validations import Post as PostSchema  # ✅ Pydantic model
from config.data_base import get_db
from models.user_model import Post

post_routes = APIRouter()

@post_routes.post("/create")
def create_post(post:PostSchema , db:Session =Depends(get_db)):
    try:
        new_post = Post(
            title = post.title,
            content = post.content,
            author_name = post.author_name
        )
        db.add(new_post)
        db.commit()
        db.refresh(new_post)

        return {
            "data":{
                "title":new_post.title,
                "content":new_post.content,
                "author_name":new_post.author_name
            },
            "massege":" Post create successfully",
            "status":"ok"
        }
    except Exception as e :
        return{
        "massege":str(e),
        "data":None,
        "status":"erorr"
        }
