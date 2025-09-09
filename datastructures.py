
#list
my_list = [1, 2, 3]
my_list.append(4) # add to end
my_list.insert(0, 0) # add at index 0
my_list.remove(2) # remove first occurrence of value 2
my_list.pop(1) # remove at index 1 (2)
my_list.sort() # sort the list (return none)
value = my_list.pop() # remove and return last item
value2 = my_list.pop(0) # remove and return item at index 0 (1)
print (value) # 4
# stupid #1???
my_list2 = my_list + [5, 6] # concatenate lists
my_list.extend(my_list2) # extend list by appending elements from the iterable



#tuple (immutable list)
my_tuple = (1, 2, 3)
print(my_tuple[0]) # 1
#my_tuple[0] = 0 # TypeError: 'tuple' object does not support item assignment

# set (unordered collection of unique items)
# hashable types only (can be keys in dictionary)
my_set = {1, 2, 3}
my_set.add(4) # add item
my_set.remove(2) # remove item
set2 = set() # empty set
print(my_set) # {1, 3, 4}
print(2 in my_set) # False
print(3 in my_set) # True

# dictionary (key-value pairs) (hashmap)
my_dict = {"name": "John", "age": 30}
#hashable types (can be keys): strings, numbers, tuples
#unhashable types (cannot be keys): lists, sets, dictionaries
#note: values can be ANY type!
# hashmap {int, set}
unique_map = {1: {1, 2, 3}, 2: {4, 5}}

my_dict["age"] = 31 # update value Note: can't increment a non-existent element
my_dict["city"] = "New York" # add key-value pair
del my_dict["name"] # remove key-value pair
len(my_dict) # returns length of dictionary
print(my_dict) # {'age': 31, 'city': 'New York'}
print("age" in my_dict) # True (containsKey) equivalent my_dict.get("city") is not None
print(my_dict.get("name")) # None (safer than my_dict["name"]) 


#iterate through dictionary (defaultly goes thru keys)
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values(): # iterate values only
    print(value)


#queue (first in first out, tunnel)
from collections import deque
queue = deque()
queue.append(1) # from right [1]
queue.append(2) # [1,2]
item = queue.popleft() # dequeue from left pop (is from right)
print(item) # 1
item = queue.popleft()
print(item) # 2

#looping a queue until its empty
while queue:
    queue.popleft() 


#stack (Last in = first out, laying bricks)
stack = []
stack.append(1) # push
stack.append(2)
item = stack.pop() # pop
print(item) # 2
item = stack.pop()
print(item) # 1

#2d list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][0]) # 1
#initialize 2d list
m = 3 # number of rows
n = 4 # number of columns
matrix = [[0 for _ in range(n)] for _ in range(m)]



def print_matrix(list_2d):
    for row in list_2d:
        for item in row:
            print(item, end=" ")
        print() # new line  

#graphs (something with a lot of connected nodes but can loop back)

#trees (linkedlist but with 2+ nodes, nothing can loop back)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#binary tree (only 2 nodes)
#binary search tree (A binary tree in which for each node, 
# all elements in its left subtree are less than the node, 
# and all elements in its right subtree are greater than the node.)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)



#example (sum of trees, recursion is default)
def find_sum(root):
    if(root == None):
        return 0
    else:
        return root.val + find_sum(root.left) + find_sum(root.right)
        

print("trees ex:")
print("summ of tree is : " + str(find_sum(root)))


# graph (directed):
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []  # List of GraphNode

# Example usage
nodeA = GraphNode('A')
nodeB = GraphNode('B')
nodeC = GraphNode('C')
nodeA.neighbors.append(nodeB)
nodeA.neighbors.append(nodeC)
nodeB.neighbors.append(nodeC)
print("graph ex:")
print("node A neighbors: " + str([n.val for n in nodeA.neighbors]))  # Output: ['B', 'C']


# adjacency list (use hashmap/dictionary), enables you to run dfs/bfs
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': []
}
# DFS function
def dfs(node, visited):
    if node in visited:
        return
    print("Visiting:", node)
    visited.add(node)
    for neighbor in graph.get(node, []):
        dfs(neighbor, visited)

# BFS function
def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited
