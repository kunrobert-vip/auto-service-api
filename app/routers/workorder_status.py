from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.workorder import WorkOrder

router = APIRouter(prefix="/workorders", tags=["workorder_status"])

VALID_STATUSES = [
    "open",
    "in_progress",
    "waiting_for_parts",
    "done",
    "delivered"
]

@router.patch("/{workorder_id}/status")
def update_workorder_status(workorder_id: int, status: str, db: Session = Depends(get_db)):
    if status not in VALID_STATUSES:
        return {"error": f"Invalid status. Valid statuses: {VALID_STATUSES}"}

    workorder = db.query(WorkOrder).filter(WorkOrder.id == workorder_id).first()
    if not workorder:
        return {"error": "Work order not found"}

    workorder.status = status
    db.commit()
    db.refresh(workorder)

    return {
        "id": workorder.id,
        "status": workorder.status
    }