# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
#
# # A function that can work with any 'Animal'
# def make_sound(animal):
#     print(animal.speak())
#
#
# # Creating objects of different classes
# dog = Dog()
# cat = Cat()
#
# # The same function call produces different results
# make_sound(dog)  # Output: Woof!
# make_sound(cat)  # Output: Meow!
#
#
#
# class Duck:
#     def quack(self):
#         print("Quack!")
#
# class Person:
#     def quack(self):
#         print("The person imitates a duck's quack.")
#
# def make_it_quack(obj):
#     obj.quack()
#
# d = Duck()
# p = Person()
#
# make_it_quack(d)  # Output: Quack!
# make_it_quack(p)  # Output: The person imitates a duck's quack.


# # Parent Class (Superclass)
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("This animal makes a sound.")
#
# # Child Class (Subclass) inheriting from Animal
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Call the parent class's constructor
#         super().__init__(name)
#         self.breed = breed
#
#     # The 'speak' method is overridden for the Dog class
#     def speak(self):
#         print(f"{self.name} the {self.breed} says Woof!")
#
# # Create instances of the classes
# my_animal = Animal("Generic Animal")
# my_dog = Dog("Buddy", "Golden Retriever")
#
# my_animal.speak() # Output: This animal makes a sound.
# my_dog.speak()    # Output: Buddy the Golden Retriever says Woof!

# # Multiple Inheritance Example
# class GasEngine:
#     def __init__(self):
#         self.fuel_level = 100
#
#     def refuel_gas(self):
#         self.fuel_level = 100
#         print("Gas tank is full.")
#
#     def run_on_gas(self):
#         print("Running on gasoline engine.")
#
# class ElectricMotor:
#     def __init__(self):
#         self.battery_charge = 100
#
#     def recharge_battery(self):
#         self.battery_charge = 100
#         print("Battery is fully charged.")
#
#     def run_on_electric(self):
#         print("Running on electric motor.")
#
# # The HybridCar class inherits from both parent classes
# class HybridCar(GasEngine, ElectricMotor):
#     def __init__(self):
#         # Call the constructors of both parent classes
#         GasEngine.__init__(self)
#         ElectricMotor.__init__(self)
#         print("Hybrid car is ready!")
#
#     def drive(self, mode):
#         if mode == "gas":
#             self.run_on_gas()
#         elif mode == "electric":
#             self.run_on_electric()
#         else:
#             print("Invalid driving mode.")
#
# # Create an instance of the child class
# my_hybrid = HybridCar()
#
# # The hybrid car can now use methods from both parent classes
# my_hybrid.refuel_gas()
# my_hybrid.recharge_battery()
#
# # It also has its own methods
# my_hybrid.drive("electric") # Output: Running on electric motor.
# my_hybrid.drive("gas")     # Output: Running on gasoline engine.

# # Using Abstract Base Classes (ABCs) to define interfaces
# from abc import ABC, abstractmethod
#
# # The abstract class 'Vehicle' provides a blueprint
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass  # No implementation here, just a declaration
#
#     @abstractmethod
#     def stop_engine(self):
#         pass
#
# # The 'Car' class provides a concrete implementation
# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started with a key.")
#
#     def stop_engine(self):
#         print("Car engine stopped.")
#
# # The 'Motorcycle' class provides a different implementation
# class Motorcycle(Vehicle):
#     def start_engine(self):
#         print("Motorcycle engine started with a kickstarter.")
#
#     def stop_engine(self):
#         print("Motorcycle engine stopped.")
#
# # This would raise a TypeError: Can't instantiate abstract class Vehicle
# # my_vehicle = Vehicle()
#
# # We can create instances of the concrete subclasses
# my_car = Car()
# my_car.start_engine()  # Output: Car engine started with a key.
#
# my_bike = Motorcycle()
# my_bike.start_engine() # Output: Motorcycle engine started with a kickstarter.

# # Encapsulation
# class PublicExample:
#     def __init__(self, name):
#         self.name = name  # Public attribute
#
# obj = PublicExample("Alice")
# print(obj.name)  # Output: Alice
# obj.name = "Bob"
# print(obj.name)  # Output: Bob
#
# class ProtectedExample:
#     def __init__(self, value):
#         self._value = value # Protected attribute
#
# obj = ProtectedExample(10)
# print(obj._value) # Output: 10 (Access is possible, but not recommended)
#
# class PrivateExample:
#     def __init__(self, balance):
#         self.__balance = balance # Private attribute
#
#     def get_balance(self):
#         return self.__balance
#
# account = PrivateExample(500)
# # print(account.__balance) # This will raise an AttributeError
#
# # The correct way is to use a public method
# print(account.get_balance()) # Output: 500
#
# # You can technically still access it via the mangled name, but it's a poor practice
# print(account._PrivateExample__balance) # Output: 500


# # Banking System Example with OOP Principles
# from abc import ABC, abstractmethod
#
# class Account(ABC):
#     def __init__(self, owner, balance=0):
#         self._owner = owner
#         self._balance = balance
#
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
#     def get_balance(self):
#         return self._balance
#
# class SavingsAccount(Account):
#     def deposit(self, amount):
#         self._balance += amount
#         print(f"Deposited ${amount} to savings. New balance: ${self._balance}")
#
#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#             print(f"Withdrew ${amount} from savings. New balance: ${self._balance}")
#         else:
#             print("Insufficient funds in savings.")
#
# class CheckingAccount(Account):
#     def deposit(self, amount):
#         self._balance += amount
#         print(f"Deposited ${amount} to checking. New balance: ${self._balance}")
#
#     def withdraw(self, amount):
#         # Overdraft allowed up to $100
#         if self._balance + 100 >= amount:
#             self._balance -= amount
#             print(f"Withdrew ${amount} from checking. New balance: ${self._balance}")
#         else:
#             print("Overdraft limit exceeded.")
#
# # Usage
# alice_savings = SavingsAccount("Alice", 500)
# alice_savings.deposit(200)
# alice_savings.withdraw(100)
#
# bob_checking = CheckingAccount("Bob", 100)
# bob_checking.withdraw(20)
# bob_checking.deposit(50)


# Library System Example with OOP Principles
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} returned.")
        else:
            print(f"{self.title} was not checked out.")

class Member:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book):
        if len(self.books) < 3:
            if not book._is_checked_out:
                book.check_out()
                self.books.append(book)
            else:
                print(f"{book.title} is already checked out.")
        else:
            print(f"{self.name} can't borrow more than 3 books.")

    def return_book(self, book):
        if book in self.books:
            book.return_book()
            self.books.remove(book)

# Usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
member = Member("Charlie")
member1 = Member("David")
member.borrow_book(book1)
member.borrow_book(book2)
member.return_book(book1)
member1.borrow_book(book2)