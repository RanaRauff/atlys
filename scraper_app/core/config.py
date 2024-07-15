import os

TOKEN = "static_token"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
