from pydantic import BaseModel

class WorkOrderPartBase(BaseModel):
    workorder_id: int
    part_id: int
    quantity: int

class WorkOrderPartCreate(WorkOrderPartBase):
    pass

class WorkOrderPartOut(WorkOrderPartBase):
    id: int

    class Config:
        orm_mode = True