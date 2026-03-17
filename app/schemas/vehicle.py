from pydantic import BaseModel

class VehicleBase(BaseModel):
    license_plate: str
    brand: str
    model: str
    year: int | None = None
    vin: str | None = None
    customer_id: int

class VehicleCreate(VehicleBase):
    pass

class VehicleOut(VehicleBase):
    id: int

    class Config:
        orm_mode = True