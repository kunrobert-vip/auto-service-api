from pydantic import BaseModel

class PartBase(BaseModel):
    name: str
    price: float
    sku: str | None = None

class PartCreate(PartBase):
    pass

class PartOut(PartBase):
    id: int

    class Config:
        orm_mode = True