"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneNode(self, node: Optional['Node']) -> Optional['Node']:
        if node not in self.mapping:
            new_node = Node(node.val)
            self.mapping[node] = new_node

            for neigh in node.neighbors:
                if neigh not in self.mapping:
                    self.cloneNode(neigh)
                
                if new_node.neighbors is None:
                    new_node.neighbors = []
                
                new_node.neighbors.append(self.mapping[neigh])

        return new_node


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        self.mapping = {}
        return self.cloneNode(node)
