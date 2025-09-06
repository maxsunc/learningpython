
# example
def add(a, b):
    return a + b

#example 2 (void = no return (None))
def greet(name):
    print(f"Hello, {name}")

#example 3 default parameters
def greet(name="Guest"):
    print(f"Hello, {name}")

#example 4 tuple as parameter
def sum_all(*numbers) -> int: # returns an int
    total = 0
    for number in numbers:
        total += number
    return total

# using functions (only after defining them)
print(add(2, 3))

greet("Alice")
greet() # uses default parameter

print(sum_all(1, 2, 3, 4, 5))

#using functions with prefixed
print(add(a=5, b=7))

