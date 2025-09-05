
len([0,1,2]) #universal length function (fire)
max(1,2,3) #universal max function (fire)
min(1,2,3) #universal min function (fire)
sum([1,2,3]) #universal sum function (fire)
sorted([3,1,2]) #returns a new sorted list (fire)

#check if is a certain type
isinstance(10, int) # True
isInstance(1,str) # False
isinstance({"name": "John"}, dict) # True
isinstance(10, (int, float)) # True if int or float

#cast to a certain type
int("10") # 10 int("a") # ValueError
str(10) # "10"

#get ascii value of a character
ord("A") # returns ASCII value of character ' and " are the same"
chr(65) # returns character of ASCII value 65 = 'A'

#check if a character is a digit
"5".isdigit() # True
"a".isdigit() # False

#list
my_list = [1, 2, 3]
joined = "#".join(str(x) for x in my_list)
print(joined)  # Output: 1#2#3

#testing code (assetions)
def testing(h, bounce, window, exp):
    actual = bouncing_ball(h, bounce, window)
    assert_equals(actual, exp)

