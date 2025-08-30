ord('A') # returns ASCII value of character
chr(65) # returns character of ASCII value

#conditional statements (indentation matters)
temperature = 21
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")

# && = and (python uses 'and')
# || = or
# !  = not

#chained comparisons
if 10 < temperature < 30:
    print("It's a nice day")

#for loop
for number in range(3): # number = 0, 1, 2
    print("Hello ", number)

#break and continue
for number in range(5):
    if number == 3:
        break
    print("Hello ", number)
    continue # continue is redundant here


#while loop
i = 1
while i <= 5:
    print("Hello ", i)
    i += 1

#Iterables: list, tuple, set, dictionary, string
for item in "Python":
    print(item)

for item in [1, 2, 3]: # list
    print(item)

for item in (1, 2, 3): # tuple ??
    print(item)

for item in {1, 2, 3}: # set
    print(item)

map = {"name": "John", "age": 30} # dictionary
for key in map:
    print(key) # prints keys
    print(key, ":", {"name": "John", "age": 30}[key]) # prints key and value

#exercises
while True:
    command = input(">")
    command = command.lower()
    if command == "quit":
        break
    elif command == "hello":
        print("Hello there!")
    elif command == "help":
        print("Available commands: hello, quit, help")
    else:
        print("I don't understand that")


# iterate from 1 to 9
for i in range(1,10):
    if i % 2 == 0:
        print(i)