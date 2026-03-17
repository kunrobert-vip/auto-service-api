from pydantic import BaseModel

class WorkOrderMechanicBase(BaseModel):
    workorder_id: int
    mechanic_id: int
    hours: int | None = None

class WorkOrderMechanicCreate(WorkOrderMechanicBase):
    pass

class WorkOrderMechanicOut(WorkOrderMechanicBase):
    id: int

    class Config:
        orm_mode = True