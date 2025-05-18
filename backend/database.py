from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
db = create_engine(os.getenv('DATABASEPATH'))
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=db)
#Session = sessionmaker(bind=db)
#session = Session()

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

