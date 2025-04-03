from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("name")
    @classmethod
    def name_length(cls, value: str) -> str:
        if len(value) <= 5:
            raise ValueError("Name must be longer than 5 characters")
        return value
    
    @field_validator("password")
    @classmethod
    def password_length(cls, value: str) -> str:
        if len(value) <= 5:  # Fixed logic (previously it was <= 65, which doesn't make sense)
            raise ValueError("Password must be longer than 5 characters")
        return value


class Post(BaseModel):
    title: str
    content: str
    author_name: str
    