from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workorder import WorkOrder
from app.schemas.workorder import WorkOrderCreate, WorkOrderOut

router = APIRouter(prefix="/workorders", tags=["workorders"])

@router.post("/", response_model=WorkOrderOut)
def create_workorder(data: WorkOrderCreate, db: Session = Depends(get_db)):
    workorder = WorkOrder(**data.dict())
    db.add(workorder)
    db.commit()
    db.refresh(workorder)
    return workorder

@router.get("/", response_model=list[WorkOrderOut])
def list_workorders(db: Session = Depends(get_db)):
    return db.query(WorkOrder).all()