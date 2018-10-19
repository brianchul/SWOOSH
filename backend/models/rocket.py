from sqlalchemy import Column, Integer, String, DateTime, Float
from config.DBindex import Base


class Rockets(Base):
    __tablename__ = "rocket"
    name = Column(String(50), primary_key=True)
    cost_billion = Column(Float(3))
    producer = Column(String(50))
    build_date = Column(DateTime)
    max_payload_weight = Column(Integer)
    max_reach_height = Column(Integer)
    create_time = Column(DateTime)