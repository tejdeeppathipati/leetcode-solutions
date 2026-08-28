"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        
        stack = [node]
        clones = {node: Node(node.val)}


        while stack:
            vertex = stack.pop()

            for neighbor in vertex.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                clones[vertex].neighbors.append(clones[neighbor])

        return clones[node]
    
    