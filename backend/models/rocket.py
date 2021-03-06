from sqlalchemy import Column, Integer, String, DateTime, Float, TEXT
from config.DBindex import Base


class Rockets(Base):
    __tablename__ = "rocket"
    
    name = Column(String(50), primary_key=True, unique=True)
    cost_billion = Column(Float(3))
    producer = Column(String(50))
    build_date = Column(DateTime)
    rocket_max_payload_weight = Column(Integer)
    rocket_max_reach_height = Column(Integer)
    status = Column(TEXT)
