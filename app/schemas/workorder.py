from pydantic import BaseModel

class WorkOrderBase(BaseModel):
    description: str
    customer_id: int
    vehicle_id: int

class WorkOrderCreate(WorkOrderBase):
    pass

class WorkOrderOut(WorkOrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True