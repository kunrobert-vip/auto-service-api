from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class WorkOrderPart(Base):
    __tablename__ = "workorder_parts"

    id = Column(Integer, primary_key=True, index=True)
    workorder_id = Column(Integer, ForeignKey("workorders.id"), nullable=False)
    part_id = Column(Integer, ForeignKey("parts.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    workorder = relationship("WorkOrder")
    part = relationship("Part")