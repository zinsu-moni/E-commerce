from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class CreateUser(BaseModel):
    full_name: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=25)
    role: str = Field(default="User", max_length=50)

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

class AdminLogin(BaseModel):
    email: EmailStr
    password: str =Field(min_length=6, max_length=25)

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category: Optional[str] = None
    image_url: Optional[str] = None
    image_public_id: Optional[str] = None
    images: Optional[List[str]] = []


class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: int
    category: Optional[str]
    image_url: Optional[str]
    image_public_id: Optional[str]
    images: Optional[List[str]]

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category: Optional[str] = None
    image_url: Optional[str] = None
    image_public_id: Optional[str] = None
    images: Optional[List[str]] = []


class CartItem(BaseModel):
    product_id: str
    quantity: int


class CartItemResponse(BaseModel):
    id: str
    user_id: int
    product_id: str
    quantity: int

    class Config:
        from_attributes = True

class CartItemUpdate(BaseModel):
    quautity: str

