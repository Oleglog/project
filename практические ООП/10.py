class ShoppingCart:
    def __init__(self):
        self.items = []  # Список товаров
    
    def add_item(self, item):
        self.items.append(item)  # Добавление товара в корзину

    def __len__(self):
        return len(self.items)  # Возвращаем количество товаров в корзине

# Пример использования
cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
print(len(cart))  # Выведет 2

class Book:
    def __init__(self, title, author, pages):
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.pages = pages  # Количество страниц

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}"  # Человекоориентированное представление

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"  # Техническое представление для отладки

    def __len__(self):
        return self.pages  # Количество страниц

# Пример использования
book = Book("1984", "George Orwell", 328)
print(book)  # Выведет: Book: 1984, Author: George Orwell, Pages: 328
print(repr(book))  # Выведет: Book(title='1984', author='George Orwell', pages=328)
print(len(book))  # Выведет 328