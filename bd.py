import table
import insert_data


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:XXXXXXX@localhost:5432/netology_db'
engine = create_engine(DSN)


table.create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([insert_data.publisher1, insert_data.publisher2, insert_data.publisher3]) #Добавляем объекты в сессию, которые хотим добавить в базу данных
session.commit()


session.close #Обязательно закрываем сессию