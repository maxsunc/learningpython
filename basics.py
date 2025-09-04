#recursion
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # optional means you can pass in nothing or return nothing
    # base case
    if root == None:
        return root
    else:
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # invert the left and right nodes
        self.invertTree(root.left) # recursion
        self.invertTree(root.right)
        return root