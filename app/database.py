import os
import time
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

password = os.getenv("DB_PASSWORD")
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{password}@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:   
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', 
#             password=os.getenv("DB_PASSWORD"), cursor_factory=RealDictCursor
#         )

#         cursor = conn.cursor()
#         print("Database connection was successfull")
#         break

#     except Exception as error:
#         print("Connection failed")
#         print("Error: ", error)
#         time.sleep(2)