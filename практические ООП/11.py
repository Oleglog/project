class List(list):
    def __add__(self, other):
        """Добавляем объект в список"""
        if isinstance(other, list):  # Проверка, что other - это список
            self.extend(other)  # Используем extend, чтобы добавить все элементы
        else:
            self.append(other)  # Иначе добавляем один элемент
        return self

    def __sub__(self, other):
        """Удаляем объект из списка"""
        if other in self:
            self.remove(other)
        return self

    def __mul__(self, other):
        """Делим список на несколько частей (большинство)"""
        if isinstance(other, int) and other > 0:
            length = len(self) // other
            return [self[i:i + length] for i in range(0, len(self), length)]
        return self

# Пример использования:
lst = List([1, 2, 3, 4])
lst + [5]  # Добавим 5
print(lst)  # [1, 2, 3, 4, 5]
lst - 2  # Удалим 2
print(lst)  # [1, 3, 4, 5]
print(lst * 2)  # Разделим список на 2 части

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __add__(self, value):
        """Добавляем элемент в конец списка"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return self

    def __sub__(self, value):
        """Удаляем элемент по значению"""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return self
            prev = current
            current = current.next
        return self

    def __str__(self):
        """Выводим элементы списка"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)

# Пример использования:
ll = LinkedList()
ll + 1 + 2 + 3  # Добавляем элементы
print(ll)  # Выведет: 1 -> 2 -> 3
ll - 2  # Удаляем элемент
print(ll)  # Выведет: 1 -> 3