from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgres://qkiqebtcwazlxo:c3dc5b7b2f5bb613c21d053c5ab67aa11a74fd864409c86ff483825eeb9b24a7@ec2-54-174-31-7.compute-1.amazonaws.com:5432/d26mc3p1uaojah"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()