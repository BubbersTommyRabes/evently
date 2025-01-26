from sqlalchemy import NullPool, create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

from orm import Base

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL, poolclass=NullPool)

def setup_database():
  try:
    with engine.connect() as connection:
      print("Connection successful!")
      Base.metadata.create_all(engine)
  except Exception as e:
    print(f"Failed to connect: {e}")
  
def get_session():
  with Session(engine) as session:
    yield session
    session.close()