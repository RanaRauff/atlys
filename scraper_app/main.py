from fastapi import FastAPI
import uvicorn
from api.endpoints import router
from services.database import init_db

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    init_db()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
