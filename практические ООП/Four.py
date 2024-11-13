class LimitedInstances:
    _instances = []
    _max_instances = 5

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < cls._max_instances:
            instance = super().__new__(cls)
            cls._instances.append(instance)
            return instance
        else:
            return cls._instances[-1]  # Возвращаем последний созданный объект


obj1 = LimitedInstances()
obj2 = LimitedInstances()
obj3 = LimitedInstances()
obj4 = LimitedInstances()
obj5 = LimitedInstances()
obj6 = LimitedInstances()  # Этот объект не будет создан, вернется пятый объект

print(obj1 is obj2)  # False
print(obj5 is obj6)  # True
print(len(LimitedInstances._instances))  # 5

class Book:
    _books = set()

    def __init__(self, title, author, year):
        if (title, author) in self._books:
            raise ValueError("Книга с таким заголовком и автором уже существует.")
        self.title = title
        self.author = author
        self.year = year
        self._books.add((title, author))


try:
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Animal Farm", "George Orwell", 1945)
    book3 = Book("1984", "George Orwell", 1949)
except ValueError as e:
    print(e)  # Вывод: Книга с таким заголовком и автором уже существует.