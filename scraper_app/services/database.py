from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model.product import Base, Product

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

class Database:
    def __init__(self):
        self.session: Session = SessionLocal()

    def save_products(self, products):
        print("productsproductsproductsproductsproducts",products)        
        for product in products:
            db_product = self.session.query(Product).filter(Product.product_title == product['product_title']).first()
            if db_product:
                db_product.product_price = product['product_price']
                db_product.image_url = product['image_url']
            else:
                db_product = Product(**product)
            self.session.merge(db_product)
        self.session.commit()

    def get_product(self, title):
        return self.session.query(Product).filter(Product.product_title == title).first()

    def get_all_products(self):
        return self.session.query(Product).all()
