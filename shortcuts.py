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
