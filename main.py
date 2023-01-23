import sqlalchemy
import psycopg2
from models import create_tables

from sqlalchemy.orm import sessionmaker
from settings import PASS

DSN = PASS
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


session.close()
