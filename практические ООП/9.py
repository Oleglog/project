class Power:
    def __init__(self, n):
        self.n = n  # Сохраняем степень
    
    def __call__(self, x):
        return x ** self.n  # Возводим x в степень n

# Пример использования
power_of_3 = Power(3)
print(power_of_3(2))  # Выведет 8 (2^3)

class Repeat:
    def __init__(self, times):
        self.times = times  # Сохраняем количество повторений
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)  # Выполняем функцию self.times раз
        return wrapper

# Пример использования
@Repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Выведет:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!