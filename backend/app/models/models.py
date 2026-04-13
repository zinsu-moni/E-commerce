from sqlalchemy import Boolean, Column, Float, Integer, String, Text
from sqlalchemy import JSON
from app.db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    full_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    role = Column(String, default="User")
    

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

    
