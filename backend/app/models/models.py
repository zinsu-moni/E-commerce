from sqlalchemy import Boolean, Column, Float, Integer, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    full_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    role = Column(String, default="User")
    cart = relationship("Cart", back_populates="user")
    

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    category = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    image_public_id = Column(String, nullable=True)
    images = Column(JSON, nullable=True, default=[])
    cart = relationship("Cart", back_populates="product")

    
class Cart(Base):
    __tablename__ = "Cart"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quantity  = Column(Integer, nullable=False, default=1)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False )
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="cart")
    product = relationship("Product", back_populates="cart")

    