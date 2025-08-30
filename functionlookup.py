
len([0,1,2]) #universal length function (fire)
max(1,2,3) #universal max function (fire)
min(1,2,3) #universal min function (fire)
sum([1,2,3]) #universal sum function (fire)
sorted([3,1,2]) #returns a new sorted list (fire)

#check if is a certain type
isinstance(10, int) # True
isinstance(10.5, float) # True
isinstance("hello", str) # True
isinstance([1,2,3], list) # True
isinstance((1,2,3), tuple) # True
isinstance({1,2,3}, set) # True
isinstance({"name": "John"}, dict) # True
isinstance(10, (int, float)) # True if int or float

#cast to a certain type
int("10") # 10
int("a") # ValueError

#get ascii value of a character
ord("A") # returns ASCII value of character

#check if a character is a digit
"5".isdigit() # True
"a".isdigit() # False

