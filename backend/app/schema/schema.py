from pydantic import BaseModel, Field, EmailStr


class CreateUser(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=25)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=25)


