from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime

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



class CartItemUpdate(BaseModel):
    quantity: int

class CartItem(BaseModel):
    product_id: int
    quantity: int = Field(..., ge=1)

class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=1, description="Must be at least 1")

class CartItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)  

    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: datetime
    updated_at: datetime

