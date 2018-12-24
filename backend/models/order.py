from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, TEXT
from sqlalchemy.orm import relationship
from config.DBindex import Base
from models import client, mission


class ClientOrders(Base):
    __tablename__ = "client_order"
    satellite_name = Column(String(100))
    weight_kg = Column(Integer)
    purpose = Column(String(500))
    request_by = Column(Integer, ForeignKey("client.id", use_alter=True))
    eta_height_km = Column(String(100))
    arrival_date = Column(DateTime)
    inclination = Column(String(50))
    budget_billion = Column(String(100))
    launch_day = Column(DateTime)
    status = Column(TEXT)


class MissionOrders(Base):
    __tablename__ = "mission_orders"
    order_id = Column(Integer, ForeignKey("client.id", use_alter=True))
    mission_id = Column(Integer, ForeignKey("mission.id", use_alter=True))
    limit_weight = Column(String(100))
    mission_arrival_deadline = Column(DateTime)
    seat_price = Column(String(100))
    status = Column(TEXT)
    weight_kg = Column(String(100))
    request_by = Column(Integer, ForeignKey("client.id", use_alter=True))



