from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from config.DBindex import Base
from models import client, mission


class ClientOrders(Base):
    __tablename__ = "client_order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    satellite_name = Column(String(100))
    weight_kg = Column(Integer)
    purpose = Column(String(500))
    request_by = Column(Integer, ForeignKey("client.id", use_alter=True))
    eta_height_km = Column(String(100))
    arrival_date = Column(DateTime)
    inclination = Column(String(50))
    budget_billion = Column(String(100))


class MissionOrders(Base):
    __tablename__ = "mission_orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("client_order.id", use_alter=True))
    mission_id = Column(Integer, ForeignKey("mission.id", use_alter=True))


