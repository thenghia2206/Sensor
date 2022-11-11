from database import Base
from sqlalchemy import Column,Integer,Float


class Sensor(Base):
    __tablename__= "sensor"
    id = Column(Integer, primary_key=True, nullable=False)
    temperature=Column(Float, nullable=False) 
    humidity=Column(Float, nullable=False)