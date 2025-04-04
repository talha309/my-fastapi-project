from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from validation.validations import User as UserSchema  # ✅ Pydantic model
from config.data_base import get_db
from models.user_model import User  # ✅ SQLAlchemy model

user_routes = APIRouter()

@user_routes.post("/register")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    try:
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password  # ⚠️ You should hash passwords before storing them!
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "data": {
                "id":new_user.id,
                "name": new_user.name,
                "email": new_user.email,
                "password":new_user.password
            },
            "message": "User successfully registered",
            "status": "ok"
        }

    except Exception as e:
        db.rollback()  # ✅ Rollback the transaction on error
        raise HTTPException(status_code=500, detail=str(e))  # ✅ Return a proper HTTP response
