from pydantic import BaseModel

class MechanicBase(BaseModel):
    name: str
    specialization: str | None = None
    hourly_rate: int | None = None

class MechanicCreate(MechanicBase):
    pass

class MechanicOut(MechanicBase):
    id: int

    class Config:
        orm_mode = True