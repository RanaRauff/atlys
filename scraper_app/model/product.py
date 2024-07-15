from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    product_title = Column(String, primary_key=True, index=True)
    product_price = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
