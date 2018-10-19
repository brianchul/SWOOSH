from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from config.DBindex import Base
from models import client, mission


class ClientOrders(Base):
    __tablename__ = "client_order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    satellite_name = Column(String(100))
    weight_kg = Column(Integer)
    purpose = Column(String(500))
    request_by = Column(Integer, ForeignKey("client.id"))
    eta_height_km = Column(Float(2))
    arrival_date = Column(DateTime)
    inclination = Column(String(50))
    create_time = Column(DateTime)


class MissionOrders(Base):
    __tablename__ = "mission_orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("client_order.id"))
    mission_id = Column(Integer, ForeignKey("mission.id"))
    create_time = Column(DateTime)

