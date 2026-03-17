from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class WorkOrderMechanic(Base):
    __tablename__ = "workorder_mechanics"

    id = Column(Integer, primary_key=True, index=True)
    workorder_id = Column(Integer, ForeignKey("workorders.id"), nullable=False)
    mechanic_id = Column(Integer, ForeignKey("mechanics.id"), nullable=False)
    hours = Column(Integer, nullable=True)  # opcionális: hány órát dolgozott

    workorder = relationship("WorkOrder")
    mechanic = relationship("Mechanic")