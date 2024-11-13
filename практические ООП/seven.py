class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self._balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма депозита не может быть отрицательной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount


class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    @property
    def price_with_discount(self):
        return self.price * (1 - self.discount / 100)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Скидка должна быть от 0% до 100%.")
        self._discount = value


class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 30000:
            raise ValueError("Зарплата должна быть не менее 30 000.")
        self._salary = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @age.deleter
    def age(self):
        self._age = None

    def apply_raise(self, percentage):
        if percentage < 0:
            raise ValueError("Процент повышения не может быть отрицательным.")
        self.salary *= (1 + percentage / 100)



if __name__ == "__main__":
    
    account = BankAccount(1000)
    print(account.balance)  # 1000
    account.deposit(500)
    print(account.balance)  # 1500
    account.withdraw(200)
    print(account.balance)  # 1300

    
    product = Product("Laptop", 1000, 10)
    print(product.price_with_discount)  # 900.0
    product.price = 1200
    product.discount = 15
    print(product.price_with_discount)  # 1020.0

  
    employee = Employee("Иван", 50000, 30)
    print(employee.name)  # Иван
    print(employee.salary)  # 50000
    employee.apply_raise(10)
    print(employee.salary)  # 55000
    print(employee.age)  # 30
    del employee.age
    print(employee.age)  # None