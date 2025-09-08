
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