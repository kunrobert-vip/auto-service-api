from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.invoice import Invoice
from app.models.workorder import WorkOrder
from app.models.workorder_part import WorkOrderPart
from app.models.part import Part
from app.models.workorder_mechanic import WorkOrderMechanic
from app.models.mechanic import Mechanic
from app.schemas.invoice import InvoiceCreate, InvoiceOut

router = APIRouter(prefix="/invoices", tags=["invoices"])

def calculate_total(workorder_id: int, db: Session):
    parts = (
        db.query(WorkOrderPart, Part)
        .join(Part, WorkOrderPart.part_id == Part.id)
        .filter(WorkOrderPart.workorder_id == workorder_id)
        .all()
    )
    parts_total = sum(item.Part.price * item.WorkOrderPart.quantity for item in parts)

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

    return parts_total + labor_total

@router.post("/", response_model=InvoiceOut)
def create_invoice(data: InvoiceCreate, db: Session = Depends(get_db)):
    workorder = db.query(WorkOrder).filter(WorkOrder.id == data.workorder_id).first()
    if not workorder:
        return {"error": "Work order not found"}

    total = calculate_total(data.workorder_id, db)

    invoice = Invoice(
        workorder_id=data.workorder_id,
        total=total,
        note=data.note
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

@router.get("/", response_model=list[InvoiceOut])
def list_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()