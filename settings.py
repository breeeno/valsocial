from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

database_url = config('SQLALCHEMY_DATABASE_URI')
engine = create_engine(database_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
