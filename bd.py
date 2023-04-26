import table
import password
import insert_data


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(password.DSN)


table.create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([insert_data.publisher1, insert_data.publisher2, insert_data.publisher3]) #Добавляем объекты в сессию, которые хотим добавить в базу данных
session.commit()


session.close #Обязательно закрываем сессию