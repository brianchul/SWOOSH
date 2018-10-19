from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from config.DBindex import Base

class Clients(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    is_launch_company = Column(Boolean)
    create_time = Column(DateTime)