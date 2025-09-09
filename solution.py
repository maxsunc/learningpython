
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        


# testing
assert Solution.cloneGraph(Node(1, [Node(2), Node(3)])) == Node(1, [Node(2), Node(3)])