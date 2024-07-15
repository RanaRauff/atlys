from pydantic import BaseModel

class ProductBase(BaseModel):
    product_title: str
    product_price: str
    image_url: str

    class Config:
        orm_mode = True

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    pass
