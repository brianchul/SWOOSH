from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from config.DBindex import Base
from models import location, rocket, client


class Missions(Base):
    __tablename__ = "mission"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price_condition = Column(String(2000))
    # join_start = Column(DateTime)
    # join_deadline = Column(DateTime)
    launch_date = Column(DateTime)
    launch_location = Column(String(100), ForeignKey("launch_location.location", use_alter=True))
    launch_rocket = Column(String(50), ForeignKey("rocket.name", use_alter=True))
    status = Column(String(50))
    target_inclination = Column(Float(4))
    target_height_km = Column(Float(2))
    create_by = Column(Integer, ForeignKey("client.id", use_alter=True))



'''    詢問Q： 可以共乘 合資的條件(高度軌道需求相同)
火箭/衛星：名稱、發射時間 公斤數 高度 目的
    需求者：申請單位 連絡電話 e-mail
傾角
高度
時間
進場日    
預算
'''