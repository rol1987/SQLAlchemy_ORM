import sqlalchemy as sq
from table import Publisher, Book, Shop, Stock, Sale



publisher1 = Publisher(name = 'Пушкин') #Создаем экземпляр класса
publisher2 = Publisher(name = 'Грибоедов') #Создаем экземпляр класса
publisher3 = Publisher(name = 'Толстой') #Создаем экземпляр класса

book1 = Book(title = 'Сказка о рыбаке и рыбке', publisher = publisher1) #Создаем экземпляр класса
book2 = Book(title = 'Горе от ума', publisher = publisher2) #Создаем экземпляр класса
book3 = Book(title = 'Война и мир', publisher = publisher3) #Создаем экземпляр класса

shop1 = Shop(name = 'Рынок') #Создаем экземпляр класса
shop2 = Shop(name = 'Читай город') #Создаем экземпляр класса
shop3 = Shop(name = 'Книжная лавка') #Создаем экземпляр класса

stock1 = Stock(book = book1, shop = shop1, count = 2) #Создаем экземпляр класса
stock2 = Stock(book = book2, shop = shop3, count = 1) #Создаем экземпляр класса
stock3 = Stock(book = book2, shop = shop3, count = 2) #Создаем экземпляр класса
stock4 = Stock(book = book3, shop = shop2, count = 4) #Создаем экземпляр класса
stock5 = Stock(book = book3, shop = shop2, count = 5) #Создаем экземпляр класса
stock6 = Stock(book = book3, shop = shop2, count = 6) #Создаем экземпляр класса
stock7 = Stock(book = book1, shop = shop3, count = 21) #Создаем экземпляр класса
stock8 = Stock(book = book2, shop = shop1, count = 1) #Создаем экземпляр класса
stock9 = Stock(book = book1, shop = shop2, count = 4) #Создаем экземпляр класса
stock10 = Stock(book = book1, shop = shop1, count = 2) #Создаем экземпляр класса


sale1 = Sale(price = 200, date_sale = "01.01.2023", stock = stock1, count = 3) #Создаем экземпляр класса
sale2 = Sale(price = 550, date_sale = "02.01.2023", stock = stock2, count = 4) #Создаем экземпляр класса
sale3 = Sale(price = 500, date_sale = "03.01.2023", stock = stock3, count = 6) #Создаем экземпляр класса
sale4 = Sale(price = 450, date_sale = "04.01.2023", stock = stock4, count = 1) #Создаем экземпляр класса
sale5 = Sale(price = 300, date_sale = "05.01.2023", stock = stock5, count = 10) #Создаем экземпляр класса

