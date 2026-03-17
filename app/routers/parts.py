from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.part import Part
from app.schemas.part import PartCreate, PartOut

router = APIRouter(prefix="/parts", tags=["parts"])

@router.post("/", response_model=PartOut)
def create_part(data: PartCreate, db: Session = Depends(get_db)):
    part = Part(**data.dict())
    db.add(part)
    db.commit()
    db.refresh(part)
    return part

@router.get("/", response_model=list[PartOut])
def list_parts(db: Session = Depends(get_db)):
    return db.query(Part).all()