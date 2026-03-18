from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    workorder_id = Column(Integer, ForeignKey("workorders.id"), nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String, default="unpaid")
    created_at = Column(DateTime, default=datetime.utcnow)
    note = Column(String, nullable=True)

    workorder = relationship("WorkOrder")