from fastapi import APIRouter, Depends
from services.scraper import Scraper
from services.database import Database
from api.dependencies import get_current_user
from model.schemas import Product as ProductSchema
from typing import List

router = APIRouter()

@router.post("/scrape/")
async def start_scraping(pages: int = 5, proxy: str = None, token: str = Depends(get_current_user)):
    scraper = Scraper(pages=pages, proxy=proxy)
    scraper.run()
    return {"message": "Scraping initiated"}

@router.get("/products/", response_model=List[ProductSchema])
async def get_products(token: str = Depends(get_current_user)):
    db = Database()
    products = db.get_all_products()
    return products
