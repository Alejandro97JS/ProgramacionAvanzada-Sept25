from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Integer, String, Text, Column, ForeignKey, Boolean

class DecBase(DeclarativeBase):
    pass

class Category(DecBase):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text(), default="")
    products = relationship("Product", back_populates="category")
    is_promoted = Column(Boolean, default=False)


class Product(DecBase):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    unit_price_cents = Column(Integer)      # 13.99€ -> 1399
    stock = Column(Integer, default=0)
    description = Column(Text(), default="")
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship("Category", back_populates="products")
