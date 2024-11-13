from datetime import datetime

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self._author = author
        self.__pages = pages

    
    def get_author(self):
        return self._author

    
    def set_author(self, author):
        self._author = author

    
    def get_pages(self):
        return self.__pages

    
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным.")

    
    def display_info(self):
        return f"Название: {self.title}, Автор: {self._author}, Страницы: {self.__pages}"


class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self._year = year
        self.__mileage = mileage

    
    def get_year(self):
        return self._year

    
    def set_year(self, year):
        current_year = datetime.now().year
        if 1886 <= year <= current_year:
            self._year = year
        else:
            raise ValueError("Год выпуска должен быть между 1886 и текущим годом.")

    
    def get_mileage(self):
        return self.__mileage

    
    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            raise ValueError("Пробег не может быть отрицательным.")

    
    def display_info(self):
        return f"Модель: {self.model}, Год выпуска: {self._year}, Пробег: {self.__mileage}"

if __name__ == "__main__":
    # Пример использования Book
    book = Book("1984", "fdgdfgdrg", 328)
    print(book.display_info())
    book.set_author("fdgdfgdrg (updated)")
    book.set_pages(350)
    print(book.display_info())

    # Пример использования Car
    car = Car("Toyota Camry", 2020, 15000)
    print(car.display_info())
    car.set_year(2021)
    car.set_mileage(16000)
    print(car.display_info())