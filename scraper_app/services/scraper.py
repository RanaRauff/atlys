import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_fixed
from services.database import Database

class Scraper:
    def __init__(self, pages=5, proxy=None):
        self.pages = pages
        self.proxy = proxy
        self.base_url = "https://dentalstall.com/shop/"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
        self.verify_ssl = False  
        self.db = Database()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def fetch_page(self, page_number):
        url = f"{self.base_url}?page={page_number}"
        print("UUUUUUUU",url)
        response = requests.get(url, headers=self.headers, proxies=self.proxies, verify=self.verify_ssl)
        response.raise_for_status()        
        return response.text
    
    def parse_page(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")    
        productsList = []
        products = soup.select('ul.products li.product')
        for product in products:
            title_tag = product.select_one('h2.woo-loop-product__title a')
            title = title_tag.text.strip() if title_tag else "N/A"

            price_tag = product.select_one('span.price ins span.woocommerce-Price-amount')
            if not price_tag:
                price_tag = product.select_one('span.price span.woocommerce-Price-amount')
            price = price_tag.text.strip() if price_tag else "N/A"

            img_tag = product.select_one('div.mf-product-thumbnail img')
            img_url = img_tag['src'] if img_tag else "N/A"
            productsList.append({"product_title": title, "product_price": price, "image_url": img_url})
        
        return productsList

    def run(self):
        all_products = []
        print("self.pagesself.pagesself.pagesself.pagesself.pages",self.pages)
        for page in range(1, self.pages + 1):
            html_content = self.fetch_page(page)
            products = self.parse_page(html_content)
            all_products.extend(products)
        self.save_to_db(all_products)
        self.notify(len(all_products))

    def save_to_db(self, products):
        updated_products = []
        for product in products:
            existing_product = self.db.get_product(product['product_title'])
            if not existing_product or existing_product.product_price != product['product_price']:
                updated_products.append(product)
        self.db.save_products(updated_products)
        self.updated_product_count = len(updated_products)

    def notify(self, product_count):
        print(f"{product_count} products scraped, {self.updated_product_count} updated and saved.")
