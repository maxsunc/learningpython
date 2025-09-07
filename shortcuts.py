from typing import Optional
# custom import
from classes import TreeNode

if not p and not q:
    print("both are None")
#equivalent to
if p is None and q is None:
    print("both are None")

class Solution:
    # you can have afunction inside of a function
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        best2 = 0
        # function within a function can access variables of the outer function
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = dfs(node.left)   # height of left subtree
            rh = dfs(node.right)  # height of right subtree
            self.best = max(self.best, lh + rh)  # diameter in edges through node
            return max(lh, rh) + 1  # height in nodes

        dfs(root)
        return self.best


# 2D array of hashmaps (dictionaries)
rows = 3
cols = 2
matrix_of_dicts = [[{} for _ in range(cols)] for _ in range(rows)]

# convert tuple to lisdt
# Convert tuple to list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# copying a list
nums = [1, 2, 3, 4]
tmpNums = list(nums) # same thing but not ref

# sorting a list
val = sorted(nums) # returns a new sorted list
tup = tuple(sorted(nums)) # returns a new sorted tuple


# get the sum of array elements
total = sum(nums[1:3]) # nums[1] + nums[2] = 5

# updating a value at dictionary even if empty:
my_dict = {}
my_dict["A"] = my_dict.get("A", 0) + 1