from sqlalchemy import Column, String, Boolean
from config.DBindex import Base


class Clients(Base):
    __tablename__ = "client"

    name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    is_launch_company = Column(Boolean)
    passwd = Column(String(32))
    username = Column(String(50), unique=True)