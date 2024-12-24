class FibonacciIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a, self.b = 0, 1  # Начальные числа Фибоначчи

    def __iter__(self):
        return self  # Итератор возвращает сам себя

    def __next__(self):
        if self.a > self.max_value:
            raise StopIteration  # Если достигнут предел, остановить итерацию
        current = self.a
        self.a, self.b = self.b, self.a + self.b  # Переход к следующему числу Фибоначчи
        return current

# Пример использования
fib = FibonacciIterator(100)
for num in fib:
    print(num)


class MultipleIterator:
    def __init__(self, multiple_of):
        self.multiple_of = multiple_of
        self.current = 0  # Начальное значение

    def __iter__(self):
        return self  # Итератор возвращает сам себя

    def __next__(self):
        self.current += self.multiple_of
        return self.current

# Пример использования
multiple_of_3 = MultipleIterator(3)
for i in range(10):  # Ограничим 10 числами
    print(next(multiple_of_3))