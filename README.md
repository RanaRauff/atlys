# My Web Scraper
This project is a web scraping tool developed using the Python FastAPI framework. It automates the process of scraping product information from the target website [Dental Stall](https://dentalstall.com/shop/).
## Project Structure

The project has the following file structure:

```
scraper_app/
├── main.py
├── api/
│   ├── __init__.py
│   ├── dependencies.py
│   ├── endpoints.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── security.py
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── schemas.py
├── services/
│   ├── __init__.py
│   ├── scraper.py
│   ├── database.py
└── requirements.txt

```

## Usage

1. Install the dependencies listed in `requirements.txt` using the command `pip install -r requirements.txt`.

2. Set the required environment variables in the `.env` file.

3. Run the application using the command `python app/main.py`.

4. Access the API endpoints to scrape and retrieve the product information.
