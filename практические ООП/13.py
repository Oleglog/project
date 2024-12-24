class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    # Переопределение метода __hash__
    def __hash__(self):
        # Используем только атрибуты title, author и publisher для хэширования
        return hash((self.title, self.author, self.publisher))

    # Переопределение метода __eq__
    def __eq__(self, other):
        if isinstance(other, Book):
            # Сравниваем книги по хэшу
            return hash(self) == hash(other)
        return False

    # Для удобства вывода
    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Year: {self.year}"

# Пример использования:
book1 = Book("Python Basics", "John Doe", "Tech Books", 2020)
book2 = Book("Python Basics", "John Doe", "Tech Books", 2020)
book3 = Book("Advanced Python", "Jane Smith", "Code Press", 2021)

# Проверка работы метода __eq__
print(book1 == book2)  # True, так как хэш и атрибуты одинаковые
print(book1 == book3)  # False, так как хэши и атрибуты разные

# Проверка работы метода __hash__
book_set = {book1, book2, book3}
print(len(book_set))  # 2, так как book1 и book2 одинаковы по хэшу и равны