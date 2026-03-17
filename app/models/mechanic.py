from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Mechanic(Base):
    __tablename__ = "mechanics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=True)  # pl. motor, futómű, elektronika
    hourly_rate = Column(Integer, nullable=True)    # óradíj (később fontos lesz)