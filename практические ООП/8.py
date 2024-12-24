class Product:
    _id_counter = 1
    
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance._id = cls._id_counter
        cls._id_counter += 1
        return instance
    
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    
    def __setattr__(self, name, value):
        if name in ["weight", "price"] and value < 0:
            raise ValueError(f"{name} cannot be negative")
        if name == "name" and not isinstance(value, str):
            raise TypeError("Name must be a string")
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        if name == "_id":
            raise AttributeError("Cannot delete 'id' attribute")
        super().__delattr__(name)

class Shop:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        self.products[product._id] = product
    
    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product not found")

class Library:
    def __init__(self, name, max_books):
        self.name = name
        self.max_books = max_books
        self.books = []
    
    def __setattr__(self, name, value):
        if name == "max_books" and hasattr(self, "max_books"):
            raise AttributeError("Cannot modify max_books after initialization")
        if name == "books" and len(value) > self.max_books:
            raise ValueError("Cannot add more books than max_books allows")
        super().__setattr__(name, value)
    
    def __getattribute__(self, name):
        print(f"Accessing attribute: {name}")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        return f"{name} not found in library"
    
    def __delattr__(self, name):
        print(f"Deleting attribute: {name}")
        if name == "name":
            raise AttributeError("Cannot delete the 'name' attribute")
        super().__delattr__(name)
    
    def add_book(self, book):
        if len(self.books) < self.max_books:
            self.books.append(book)
        else:
            raise ValueError("Library is full")
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError("Book not found")
    
    def list_books(self):
        return self.books