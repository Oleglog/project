import re
from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(card_number):
        # Шаблон для проверки номера карты (например, 16 цифр)
        pattern = r'^\d{16}$'
        return bool(re.match(pattern, card_number))

    @classmethod
    def check_name(cls, name):
        # Проверка имени и фамилии
        pattern = r'^[{} ]+$'.format(cls.CHARS_FOR_NAME)
        return bool(re.match(pattern, name))


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def from_kelvin(cls, kelvin):
        celsius = kelvin - 273.15
        return celsius


class Employee:
    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 65

    @classmethod
    def from_string(cls, data):
        name, age_str, position = data.split(',')
        age = int(age_str)
        if not cls.is_valid_age(age):
            raise ValueError("Возраст должен быть в диапазоне от 18 до 65 лет.")
        return cls(name, age, position)

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def get_details(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}"
    
if __name__ == "__main__":
    print(CardCheck.check_card_number("1234567812345678"))
    print(CardCheck.check_name("Иван Иванов"))

    
    print(TemperatureConverter.celsius_to_fahrenheit(25))
    print(TemperatureConverter.from_kelvin(300))

    
    try:
        emp = Employee.from_string("Иван, 30, Менеджер")
        print(emp.get_details())
    except ValueError as e:
        print(e)