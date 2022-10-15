from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.types import Date
from api.db import Base

class Area(Base):
    __tablename__ = "personnel_area"

    id = Column(Integer, primary_key=True)
    area_code = Column(String(255), index=True)
    area_name = Column(String(255))
    parent_area = Column(String(255))
    
class Transactions(Base):
    __tablename__ = "iclock_transaction"
    
    id = Column(Integer, primary_key=True)
    emp_code = Column(String(255), index=True)
    punch_time = Column(DateTime, index=True)
    terminal_sn = Column(String(255))
    area_alias = Column(String(255))
    upload_time = Column(DateTime)
    reserved = Column(String(255))
    