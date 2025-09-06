from collections import deque

#trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#BFS checks level count fo tree first (using queue) ( leftmost bfs)
#If you're optimizing to find the shortest possible route 

def walkBFS(tree):
    queue = deque()
    queue.append(tree)
    while queue:
        node = queue.popleft() # pop the left node
        if node is not None:
            # add the left and right values to queue (will be accessed later) lest they're None print node cuz we accessed it from queue
            print(node.val)
            queue.append(node.left)
            queue.append(node.right)



#DFS checks children first (3 versions, pre order, in order, post order)
# Time complexity O(n) n = number of nodes
# Space complexity O(h) h = height of tree (worst case O(n) for
# when we want to know if a route exists
# every DFS uses a stack
#first method 
def walk(tree):
    if tree is not None:
        print(tree.val) # pre order
        walk(tree.left)
        # print(tree.val) # in order
        walk(tree.right)
        # print(tree.val) post order
# second method
def walkIterative(tree):
    # use our own stack
    stack = []
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop # take the node off the stack
        if node is not None:
            print(node.val)
            stack.append(node.right) 
            stack.append(node.left) # appending None doesn't add anything to the stack
        

tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(2)
walk(tree)

print("printing bfs")
tree = TreeNode(0)
tree.left = TreeNode(1)
tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
walkBFS(tree)

#e.x. checking if it has a path