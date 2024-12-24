class KeyValueStore:
    def __init__(self):
        self.store = {}  # Словарь для хранения данных

    def __getitem__(self, key):
        """Получение значения по ключу"""
        return self.store[key]

    def __setitem__(self, key, value):
        """Установка значения для ключа"""
        self.store[key] = value
        self.log_change(f"Set: {key} = {value}")

    def __delitem__(self, key):
        """Удаление элемента по ключу"""
        value = self.store.pop(key)
        self.log_change(f"Deleted: {key} = {value}")

    def log_change(self, log_message):
        """Запись изменений в файл"""
        with open("log.txt", "a") as file:
            file.write(log_message + "\n")

    def __str__(self):
        """Строковое представление объекта"""
        return str(self.store)

# Пример использования:
kv_store = KeyValueStore()

# Добавление элементов
kv_store["apple"] = 10
kv_store["banana"] = 20

# Чтение элемента
print(kv_store["apple"])  # 10

# Удаление элемента
del kv_store["banana"]

# Содержание файла log.txt после выполнения
# Set: apple = 10
# Set: banana = 20
# Deleted: banana = 20