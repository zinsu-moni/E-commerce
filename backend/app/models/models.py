from sqlalchemy import Boolean, Column, Float, Integer, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
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


class OrderStatus(Base):
    __tablename__  = "Order"

    pending = Column(Integer, primary_key=True, nullable=False)
    shipped = Column(Integer, primary_key=True, nullable=False)
    delivered = Column(Integer, primary_key=True, nullable=False)
    cancelled = Column(Integer, primary_key=True, nullable=False)
    


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    reference = Column(String, unique=True, nullable=False, index=True)
    status = Column(String, default="pending", nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="NGN", nullable=False)
    shipping_address = Column(JSON, nullable=True)
    delivery_notes = Column(String, nullable=True)
    save_address = Column(Boolean, default=False)
    provider = Column(String, nullable=True)
    provider_transaction_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, nullable=False)
    order = relationship("Order", back_populates="items")

