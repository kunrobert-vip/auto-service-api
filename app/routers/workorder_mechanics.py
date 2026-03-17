from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workorder_mechanic import WorkOrderMechanic
from app.schemas.workorder_mechanic import WorkOrderMechanicCreate, WorkOrderMechanicOut

router = APIRouter(prefix="/workorder-mechanics", tags=["workorder_mechanics"])

@router.post("/", response_model=WorkOrderMechanicOut)
def assign_mechanic_to_workorder(data: WorkOrderMechanicCreate, db: Session = Depends(get_db)):
    item = WorkOrderMechanic(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/", response_model=list[WorkOrderMechanicOut])
def list_workorder_mechanics(db: Session = Depends(get_db)):
    return db.query(WorkOrderMechanic).all()