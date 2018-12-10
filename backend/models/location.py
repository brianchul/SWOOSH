from sqlalchemy import Column, String, DateTime
from config.DBindex import Base


class LaunchLocations(Base):
    __tablename__ = "launch_location"
    observate_location = Column(String(100))
    location = Column(String(100), primary_key=True, unique=True)
    country = Column(String(50))

