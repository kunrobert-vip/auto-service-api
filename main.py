from fastapi import FastAPI
from app.routers import (
    health, customers, vehicles, workorders,
    parts, workorder_parts, mechanics,
    workorder_mechanics, calc, workorder_status
)


from app.core.database import Base, engine

# adatbázis táblák létrehozása
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auto Service API",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(customers.router)
app.include_router(vehicles.router)
app.include_router(workorders.router)
app.include_router(parts.router)
app.include_router(workorder_parts.router)
app.include_router(mechanics.router)
app.include_router(workorder_mechanics.router)
app.include_router(calc.router)
app.include_router(workorder_status.router)


@app.get("/")
def root():
    return {"message": "Auto Service API működik"}