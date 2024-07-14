from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    shop_id = Column(Integer, ForeignKey("shops.id"))


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    discount = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    dt_create = Column(DateTime, server_default=func.now())
    shop_id = Column(Integer, ForeignKey("shops.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))


class SalesUnit(Base):
    __tablename__ = "sales_units"

    id = Column(Integer, primary_key=True, index=True)
    dt_create = Column(DateTime, server_default=func.now())
    bill_id = Column(Integer, ForeignKey("bills.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    product_price = Column(Float)
    units = Column(Integer)
    total_price = Column(Float)
