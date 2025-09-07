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


# fixed sliding window (array/string)
def maxSum(arr, k):
    # find max sum of k consecutive elements in array
    if len(arr) < k:
        return None
    max_sum = 0
    window_sum = sum(arr[0:k]) # sum of first k elements, up to k-1
    # window_sum = arr[0] + arr[1] + ... + arr[k-1]
    max_sum = window_sum # initialize max_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k] # add next element, remove first element of previous window
        max_sum = max(max_sum, window_sum)
    return max_sum

# dynamic sliding window (array/string)
def minSubArrayLen(arr, s):
    # find min length of subarray with sum >= s
    n = len(arr)
    min_length = float('inf')
    window_sum = 0
    left = 0
    for right in range(n):
        window_sum += arr[right] # expnd window to the right
        while window_sum >= s: # shrink window from left as long as sum >= s
            min_length = min(min_length, right - left + 1) # update min_length
            window_sum -= arr[left] # shrink window from left
            left += 1 # move left pointer to the right
    return min_length if min_length != float('inf') else 0