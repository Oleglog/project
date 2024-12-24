class Device:
    def __init__(self, is_on, battery_level):
        self.is_on = is_on
        self.battery_level = battery_level

    # Переопределяем метод __bool__
    def __bool__(self):
        # Устройство считается истинным, если оно включено и заряд больше 10%
        return self.is_on and self.battery_level > 10

    # Для удобства вывода
    def __str__(self):
        return f"Device is {'on' if self.is_on else 'off'}, battery level: {self.battery_level}%"

# Пример использования:
device1 = Device(True, 15)  # Устройство включено и с зарядом больше 10%
device2 = Device(True, 5)   # Устройство включено, но заряд меньше 10%
device3 = Device(False, 50) # Устройство выключено, независимо от заряда

# Проверка метода __bool__
print(bool(device1))  # True, так как устройство включено и заряд > 10%
print(bool(device2))  # False, так как заряд < 10%
print(bool(device3))  # False, так как устройство выключено