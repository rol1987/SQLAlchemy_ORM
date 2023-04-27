import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    #Создание таблицы, которая будет создана в Postgres
    __tablename__ = "publisher"
    #Создание полей таблицы
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length = 40), unique = True)


class Book(Base):
    #Создание таблицы, которая будет создана в Postgres
    __tablename__ = "book"
    #Создание полей таблицы
    id = sq.Column(sq.Integer, primary_key = True)
    title = sq.Column(sq.String(length = 40), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='book')


class Shop(Base):
    #Создание таблицы, которая будет создана в Postgres
    __tablename__ = "shop"
    #Создание полей таблицы
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length = 40), unique = True, nullable=False)

class Stock(Base):
    #Создание таблицы, которая будет создана в Postgres
    __tablename__ = "stock"
    #Создание полей таблицы
    id = sq.Column(sq.Integer, primary_key = True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable = False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

class Sale(Base):
    #Создание таблицы, которая будет создана в Postgres
    __tablename__ = "sale"
    #Создание полей таблицы
    id = sq.Column(sq.Integer, primary_key = True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable = False)

    stock = relationship(Stock, backref='sale')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)