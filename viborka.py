from sqlalchemy import or_ 
# from insert_data import insert_data
from engine import session, engine #Из файла с подключением к базе импортируем сессию
from table import Publisher, Book, Shop, Stock, Sale #Из файла с моделями импортиуем необходимые модели для запроса
import table
import insert_data

def get_shops(find_publisher): #Функция принимает обязательный параметр
    items = session.query( #Создаем общее тело запроса на выборку данных и сохраняем в переменную
        Book.title, Shop.name, Sale.price, Sale.date_sale, #Название книги, имя магазина, стоимость продажи и дату продажи
    ).select_from(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher).\
        join(Sale).\
        filter(or_(
            Publisher.name == find_publisher, Publisher.id == find_publisher #Где айди публициста равно передаваемому значению в функцию или имя публициста равно передаваемому значению
        )).all()
    for a, b, c, d in items: #При каждой итерации получаем кортеж и распаковываем значения в 4 переменные
        print(f"{a: <40} | {b: <10} | {c: <8} | {d.strftime('%d-%m-%Y')}") #Передаем в фоматированную строку переменные, которые содержат имя книги, название магазина, стоимость продажи и дату продажи


if __name__ == '__main__':
    table.create_tables(engine)
    insert_data.insert_data(session)
    
    find_publisher = input("Введите имя автора или его ID: ") #Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
    get_shops(find_publisher) #Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше    
