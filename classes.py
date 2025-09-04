#classes (blueprints for creating objects)

# Basic class definition
class Person:
    # Class variable (shared by all instances (STATIC))
    species = "Homo sapiens"
    
    def __init__(self, name, age):  # Constructor
        # Instance variables (unique to each object)
        # Note: anything with self becomes Instance Variables
        #NOTE: self is needed to define a function within a class
        self.name = name
        self.age = age
    
    # Instance method
    def greet(self):
        return f"Hi, I'm {self.name}"
    
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! Now I'm {self.age}"

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)  # Alice
print(person1.age)   # 25

# Calling methods
print(person1.greet())  # Hi, I'm Alice
print(person1.have_birthday())  # Happy birthday! Now I'm 26

# Class variables are shared
print(person1.species)  # Homo sapiens
print(person2.species)  # Homo sapiens

# Inheritance (creating subclasses)
class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    # Override parent method
    def greet(self):
        return f"Hi, I'm {self.name}, student ID: {self.student_id}"
    
    # New method specific to Student
    def study(self):
        return f"{self.name} is studying"

# Using inheritance
student = Student("Charlie", 20, "S123")
print(student.greet())  # Hi, I'm Charlie, student ID: S123
print(student.study())  # Charlie is studying
print(student.have_birthday())  # Inherited method works too

# Private attributes (convention: prefix with _)
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "private" by convention
    
    def deposit(self, amount):
        self._balance += amount
    
    def get_balance(self):
        return self._balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
# print(account._balance)  # Works but shouldn't be accessed directly

# Static methods and class methods
class MathUtils:
    @staticmethod
    def add(a, b):  # Doesn't need self or cls
        return a + b
    
    @classmethod
    def from_string(cls, string_num):  # Takes cls instead of self
        return cls(int(string_num))

print(MathUtils.add(5, 3))  # 8 - can call without creating instance