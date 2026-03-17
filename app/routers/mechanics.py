from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.mechanic import Mechanic
from app.schemas.mechanic import MechanicCreate, MechanicOut

router = APIRouter(prefix="/mechanics", tags=["mechanics"])

@router.post("/", response_model=MechanicOut)
def create_mechanic(data: MechanicCreate, db: Session = Depends(get_db)):
    mechanic = Mechanic(**data.dict())
    db.add(mechanic)
    db.commit()
    db.refresh(mechanic)
    return mechanic

@router.get("/", response_model=list[MechanicOut])
def list_mechanics(db: Session = Depends(get_db)):
    return db.query(Mechanic).all()