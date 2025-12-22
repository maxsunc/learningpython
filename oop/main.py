# import Vehicle class from Vehicle.py so we can use it here
from Vehicle import Vehicle

my_vehicle = Vehicle("Toyota", "Camry", 2020, "Blue")
print(my_vehicle.make)  # Output: Toyota
my_vehicle.drive()  # Output: driving brrrr

my_vehicle.drive()