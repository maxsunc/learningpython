import math

#new ones
print(10 ** 3) # exponentiation 10^3
print(10 // 3) # floor division

round(2.9) # = 3
abs(-20) # = 20

#math module https://www.w3schools.com/python/module_math.asp
math.ceil(2.2) # = 3
math.floor(2.9) # = 2
#...

#type conversions

x = input("Enter a number: ") # input is always a string

print(type(x)) # returns type of x 
y = int(x) # cast as integer
print(type(y))




#Falsy values: 0, 0.0, "", [], {}, set(), None, False
#Truthy values: everything else