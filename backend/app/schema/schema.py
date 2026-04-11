from pydantic import BaseModel, Field, EmailStr


class CreateUser(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=25)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=25)

class VerifyOTP(BaseModel):
    email: EmailStr
    otp: str

class ForgotPassword(BaseModel):
    email: str

class ResetPassword(BaseModel):
    email: str
    new_password: str = Field(min_length=6, max_length=25)
    
class ChangePassword(BaseModel):
    current_password: str
    new_password: str = Field(min_length=6, max_length=25)

