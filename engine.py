


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:83FrkWrt@localhost:5432/netology_db'
engine = create_engine(DSN)




Session = sessionmaker(bind=engine)
session = Session()

