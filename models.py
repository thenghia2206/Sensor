from database import Base
from sqlalchemy import Column,Integer,Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
import datetime

from datetime import timedelta  

x = datetime.datetime.now() + timedelta(hours=7) 


class Sensor(Base):
    __tablename__= "sensor"
    id = Column(Integer, primary_key=True, nullable=False)
    temperature=Column(Float, nullable=False) 
    humidity=Column(Float, nullable=False)
    createdOn=Column(TIMESTAMP(timezone=True),nullable=False, default=x)
