from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workorder_part import WorkOrderPart
from app.schemas.workorder_part import WorkOrderPartCreate, WorkOrderPartOut

router = APIRouter(prefix="/workorder-parts", tags=["workorder_parts"])

@router.post("/", response_model=WorkOrderPartOut)
def add_part_to_workorder(data: WorkOrderPartCreate, db: Session = Depends(get_db)):
    item = WorkOrderPart(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/", response_model=list[WorkOrderPartOut])
def list_workorder_parts(db: Session = Depends(get_db)):
    return db.query(WorkOrderPart).all()