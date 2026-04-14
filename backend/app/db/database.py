import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "sqlite:///./ecomm.db"

engine = create_engine(DATABASE_URL)
user_engine = engine 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)
    if engine.dialect.name != "sqlite":
        return

    inspector = inspect(engine)
    
    # Migrate user table
    if "user" in inspector.get_table_names():
        existing_columns = {column["name"] for column in inspector.get_columns("user")}
        with engine.begin() as connection:
            if "is_admin" not in existing_columns:
                connection.execute(text("ALTER TABLE user ADD COLUMN is_admin BOOLEAN DEFAULT 0"))
            if "role" not in existing_columns:
                connection.execute(text("ALTER TABLE user ADD COLUMN role VARCHAR DEFAULT 'User'"))
    
    # Migrate product table - recreate if key schema is invalid
    if "product" in inspector.get_table_names():
        existing_columns = {column["name"] for column in inspector.get_columns("product")}
        id_column = next((column for column in inspector.get_columns("product") if column["name"] == "id"), None)
        recreate_product_table = False

        # If id isn't a primary key, inserts without explicit id will fail in SQLite.
        if not id_column or id_column.get("primary_key", 0) == 0:
            recreate_product_table = True

        required_columns = {"name", "description", "price", "stock", "category", "image_url", "image_public_id", "images"}
        if not required_columns.issubset(existing_columns):
            recreate_product_table = True

        with engine.begin() as connection:
            if recreate_product_table:
                connection.execute(text("DROP TABLE product"))

    # Migrate Cart table
    table_names = inspector.get_table_names()
    cart_table_name = "Cart" if "Cart" in table_names else "cart" if "cart" in table_names else None
    recreate_cart_table = False
    if cart_table_name:
        existing_columns = {column["name"] for column in inspector.get_columns(cart_table_name)}
        required_columns = {"id", "product_id", "user_id", "created_at", "updated_at"}

        if not required_columns.issubset(existing_columns):
            recreate_cart_table = True

        with engine.begin() as connection:
            if recreate_cart_table:
                # Old local schemas may have incompatible cart columns; rebuild table.
                connection.execute(text('DROP TABLE IF EXISTS "Cart"'))
                connection.execute(text('DROP TABLE IF EXISTS "cart"'))
            elif "quantity" not in existing_columns:
                connection.execute(text(f'ALTER TABLE "{cart_table_name}" ADD COLUMN quantity INTEGER DEFAULT 1'))

                # Backfill from common misspelled legacy column if present.
                if "quautity" in existing_columns:
                    connection.execute(
                        text(f'UPDATE "{cart_table_name}" SET quantity = quautity WHERE quautity IS NOT NULL')
                    )
    
    # Recreate all tables to ensure proper schema
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()                    