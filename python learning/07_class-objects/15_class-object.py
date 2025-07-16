#1. Create a Simple Class

class Dog:
    def __init__(self):
        print("A dog has been created.")

print(" ")
#2. Create an Object from a Class

my_dog = Dog()

print(" ")
#3. Initialize Attributes Using __init__

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Dog's name is {self.name} and age is {self.age}.")

my_dog = Dog("Max", 3)

print(" ")
#4. Add a Method

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

dog = Dog("Buddy")
dog.bark()

print(" ")
#5. Access Attributes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Rocky", 5)
print("Name:", my_dog.name)
print("Age:", my_dog.age)

print(" ")
#6. Student Class with Method

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student = Student("Chiz", 20, "A")
student.show_details()

print(" ")
#7. Rectangle with Area Method

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 5)
print("Area:", rect.area())

print(" ")
#8. Update Object Attribute

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def update_year(self, new_year):
        self.year = new_year

car = Car("Toyota", 2010)
car.update_year(2023)
print(car.brand, car.year)

print(" ")
#9. Use __str__ Method

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("The Alchemist", "Paulo Coelho")
print(book)

print(" ")
#10. List of Objects

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [
    Product("Phone", 700),
    Product("Laptop", 1200),
    Product("Tablet", 450)
]

for p in products:
    print(f"{p.name}: ${p.price}")

print(" ")

#11. Bank Account Class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn.")

    def check_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount("Alice")
account.deposit(500)
account.withdraw(200)
account.check_balance()

print(" ")
#12. Inheritance

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def show(self):
        print(f"{self.name} earns {self.salary}")

emp = Employee("David", 50000)
emp.show()

print(" ")
#13. Class with Class Variable

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

a = Counter()
b = Counter()
c = Counter()
print("Objects created:", Counter.get_count())

print(" ")
#14. Private Attributes

class Secret:
    def __init__(self, code):
        self.__code = code

    def reveal(self, user):
        if user == "admin":
            return self.__code
        else:
            return "Access Denied"

secret = Secret("XYZ123")
print(secret.reveal("admin"))      # Output: XYZ123
print(secret.reveal("guest"))      # Output: Access Denied

print(" ")
#15. To-Do App Class

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def show_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            print("-", task)

todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Go for a walk")
todo.show_tasks()
todo.remove_task("Go for a walk")
todo.show_tasks()