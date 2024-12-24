class Resource:
    def __init__(self, name, resource_type):
        self.name = name
        self.resource_type = resource_type

    def __del__(self):
        print(f"Resource deleted: Name = {self.name}, Type = {self.resource_type}")

r1 = Resource("Resource1", "TypeA")
r2 = Resource("Resource2", "TypeB")


print(r1.name, r1.resource_type)
print(r2.name, r2.resource_type)

for i in range(10):
    print(i)
    if i == 5:
        del r2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0 

    def len(self):
        return self.length

    def search(self, data):
        current = self.start
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def append(self, obj):
        new_node = Node(obj)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")

        current = self.start

        if index == 0:
            self.start = current.next
            if self.start is None:
                self.end = None
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if current.next is None:
                self.end = current

        self.length -= 1