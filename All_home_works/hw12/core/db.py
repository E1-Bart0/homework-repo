from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

URL = "sqlite:///main.db"
engine = create_engine(URL, echo=True)
Base = declarative_base()
