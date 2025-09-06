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
    
    # recursive Function
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1) # must call functions with self

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
    

class Vehicle:
    # class variable
    speed = 0

    # instance variable only accessible within the instance
    def __init__(self, make, model):
        self.make = make
        self.model = model