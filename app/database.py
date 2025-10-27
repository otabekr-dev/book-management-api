from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

DATABASE_URL = URL.create(
    drivername = 'postgresql+psycopg2',
    host = config.DB_HOST,
    port = config.DB_PORT,
    password = config.DB_PASS,
    username = config.DB_USER,
    database = config.DB_NAME
)

engine = create_engine(url=DATABASE_URL)
Base = declarative_base()

LocalSession = sessionmaker(bind=engine)
   
