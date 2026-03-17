from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workorder import WorkOrder
from app.models.workorder_part import WorkOrderPart
from app.models.part import Part
from app.models.workorder_mechanic import WorkOrderMechanic
from app.models.mechanic import Mechanic

router = APIRouter(prefix="/calc", tags=["calculation"])

@router.get("/workorder/{workorder_id}")
def calculate_workorder_total(workorder_id: int, db: Session = Depends(get_db)):
    # Ellenőrizzük, hogy létezik-e a munkalap
    workorder = db.query(WorkOrder).filter(WorkOrder.id == workorder_id).first()
    if not workorder:
        return {"error": "Work order not found"}

    # Alkatrészek összegzése
    parts = (
        db.query(WorkOrderPart, Part)
        .join(Part, WorkOrderPart.part_id == Part.id)
        .filter(WorkOrderPart.workorder_id == workorder_id)
        .all()
    )

    parts_total = sum(item.Part.price * item.WorkOrderPart.quantity for item in parts)

    # Szerelők összegzése
    mechanics = (
        db.query(WorkOrderMechanic, Mechanic)
        .join(Mechanic, WorkOrderMechanic.mechanic_id == Mechanic.id)
        .filter(WorkOrderMechanic.workorder_id == workorder_id)
        .all()
    )

    labor_total = sum(
        item.Mechanic.hourly_rate * item.WorkOrderMechanic.hours
        for item in mechanics
        if item.WorkOrderMechanic.hours is not None
    )

    total = parts_total + labor_total

    return {
        "workorder_id": workorder_id,
        "parts_total": parts_total,
        "labor_total": labor_total,
        "total": total
    }