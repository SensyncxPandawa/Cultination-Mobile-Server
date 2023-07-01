from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cart_id = Column(String(255), unique=True, nullable=False)
    product_id = Column(String(255), nullable=False)
    product_vendor_id = Column(String(255), nullable=False)
    user_id = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(String(255), unique=True, nullable=False)
    vendor_id = Column(String(255), nullable=False)
    category_id = Column(String(255), nullable=False)
    product_name = Column(String(255), nullable=False)
    product_description = Column(Text, nullable=False)
    product_images_path = Column(String(255), nullable=False)
    product_discount = Column(String(255), nullable=False)
    product_price = Column(String(255), nullable=False)
    product_stock = Column(String(255), nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String(255), unique=True, nullable=False)
    user_email = Column(String(255), nullable=False)
    user_password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    user_contact = Column(String(255), nullable=False)
    user_address = Column(Text, nullable=False)

class PurchaseItem(Base):
    __tablename__ = 'purchase_items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    purchase_item_id = Column(String(255), unique=True, nullable=False)
    purchase_id = Column(String(255), nullable=False)
    product_id = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)

class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vendor_id = Column(String(255), unique=True, nullable=False)
    vendor_name = Column(String(255), nullable=False)
    vendor_contact = Column(String(255), nullable=False)
    vendor_address = Column(String(255), nullable=False)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(String(255), unique=True, nullable=False)
    category_name = Column(String(255), nullable=False)

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    purchase_id = Column(String(255), unique=True, nullable=False)
    user_id = Column(String(255), nullable=False)
    total_amount = Column(Integer, nullable=False)
    purchase_date = Column(DateTime(255), nullable=False)
    purchase_status = Column(String(255), nullable=False)
