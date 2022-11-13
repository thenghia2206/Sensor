from database import Base
from sqlalchemy import Column,Integer,Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime
import pytz

tz_VN = pytz.timezone('Asia/Ho_Chi_Minh') 
datetime_VN = datetime.now(tz_VN)


class Sensor(Base):
    __tablename__= "sensor"
    id = Column(Integer, primary_key=True, nullable=False)
    temperature=Column(Float, nullable=False) 
    humidity=Column(Float, nullable=False)
    createdOn=Column(TIMESTAMP,nullable=False, default=datetime_VN )
