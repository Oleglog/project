class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Перегрузка оператора ==
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.pages == other.pages
        return NotImplemented

    # Перегрузка оператора !=
    def __ne__(self, other):
        if isinstance(other, Book):
            return self.pages != other.pages
        return NotImplemented

    # Перегрузка оператора <
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

    # Перегрузка оператора >
    def __gt__(self, other):
        if isinstance(other, Book):
            return self.pages > other.pages
        return NotImplemented

    # Перегрузка оператора <=
    def __le__(self, other):
        if isinstance(other, Book):
            return self.pages <= other.pages
        return NotImplemented

    # Перегрузка оператора >=
    def __ge__(self, other):
        if isinstance(other, Book):
            return self.pages >= other.pages
        return NotImplemented

    # Для удобства вывода
    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

# Пример использования
book1 = Book("Book One", 150)
book2 = Book("Book Two", 200)
book3 = Book("Book Three", 150)

print(book1 == book2)  # False
print(book1 != book2)  # True
print(book1 < book2)   # True
print(book2 > book1)   # True
print(book1 <= book3)  # True
print(book2 >= book1)  # True