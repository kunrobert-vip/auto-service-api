from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="Auto Service API",
    version="1.0.0"
)

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Auto Service API működik"}