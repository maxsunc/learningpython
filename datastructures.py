
#list
my_list = [1, 2, 3]
my_list.append(4) # add to end
my_list.insert(0, 0) # add at index 0
my_list.remove(2) # remove first occurrence of value 2
value = my_list.pop() # remove and return last item
value2 = my_list.pop(0) # remove and return item at index 0
print (value) # 4

#tuple (immutable list)
my_tuple = (1, 2, 3)
print(my_tuple[0]) # 1
#my_tuple[0] = 0 # TypeError: 'tuple' object does not support item assignment

# set (unordered collection of unique items)
my_set = {1, 2, 3}
my_set.add(4) # add item
my_set.remove(2) # remove item
print(my_set) # {1, 3, 4}
print(2 in my_set) # False
print(3 in my_set) # True

# dictionary (key-value pairs)
my_dict = {"name": "John", "age": 30}
my_dict["age"] = 31 # update value
my_dict["city"] = "New York" # add key-value pair
del my_dict["name"] # remove key-value pair
print(my_dict) # {'age': 31, 'city': 'New York'}
print("age" in my_dict) # True
print(my_dict.get("name")) # None (safer than my_dict["name"]) 


#queue
from collections import deque
queue = deque()
queue.append(1) # enqueue
queue.append(2)
item = queue.popleft() # dequeue only from left
print(item) # 1
item = queue.popleft()
print(item) # 2

#stack
stack = []
stack.append(1) # push
stack.append(2)
item = stack.pop() # pop
print(item) # 2
item = stack.pop()
print(item) # 1
