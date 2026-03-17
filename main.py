from fastapi import FastAPI
from app.routers import health, customers
from app.core.database import Base, engine

# adatbázis táblák létrehozása
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auto Service API",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(customers.router)

@app.get("/")
def root():
    return {"message": "Auto Service API működik"}