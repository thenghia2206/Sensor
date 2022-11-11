from fastapi import FastAPI,Depends
import models
from database import engine
from sqlalchemy.orm import Session
from database import get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get('/sensor/')
async def sensor(temp : float ,hum: float ,db: Session = Depends(get_db) ):
    x = models.Sensor(temperature = temp, humidity = hum)
    db.add(x)
    db.commit()
    db.refresh(x)
    return {'temperature': temp ,'humidity' : hum  }

@app.get('/all')
def get_all(db: Session = Depends(get_db)):
    y = db.query(models.Sensor).all()
    return y




@app.get('/')
def root_api():
    return {"message": "Welcome to The Nghia"}