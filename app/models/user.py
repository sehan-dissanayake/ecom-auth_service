from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    email: EmailStr
    password: str
    disabled: bool = False

    class Settings:
        name = "users"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserInDB(User):
    hashed_password: str