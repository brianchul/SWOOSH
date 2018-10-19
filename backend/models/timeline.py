from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.DBindex import Base
from models import rocket


class Timelines(Base):
    __tablename__ = "launch_timeline"
    id = Column(Integer, primary_key=True, autoincrement=True)
    rocket_name = Column(String(50), ForeignKey("rocket.name"))
    launch_day = Column(DateTime)
    launch_location = Column(String(50))
    mission_discription = Column(String(1000))
    create_time = Column(DateTime)
