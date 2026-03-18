from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    workorder_id: int
    note: str | None = None

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceOut(InvoiceBase):
    id: int
    total: float
    status: str
    created_at: datetime

    class Config:
        orm_mode = True