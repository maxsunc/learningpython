course = "python man"


course[0]     # access a character in course
course[-1]    # access last character in course
course[0:3]   # access a slice of characters in course
course[0:]    # access a slice from start to end
course[:]     # access a slice of the whole string

#escape sequence
#\'  \n  \t  \\

str = "super"
full = f"{str} {course}"#formatted string 

print(full)

#Methods
len(course)  # access length of course 
course.upper() # convert to uppercase
course.lower() # convert to lowercase
course.title() # convert to titlecase "Python Man"
print(course.find("man")) # find the index of the first occurrence of a substring
print(course.replace("n", "N")) # replace a substring with another substring
print("python" in course) # check if a substring exists in the string
print(course[0].islower) # true (only can return true on alphabet)