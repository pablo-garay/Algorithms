"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Runtime: 36 ms, faster than 87.52%. Memory Usage: less than 98%
class Solution(object):  # Time: O(|v| + |e|) - optimal as need to traverse the whole graph in worst case. Space: O(|v|)
    def cloneGraph(self, node):
        self.visited = {}
        return self.makeCopy(node)

    def makeCopy(self, node):
        if node is None:
            return None
        if node.val in self.visited:
            return self.visited[node.val]

        n = Node(node.val)
        self.visited[n.val] = n

        for neigh in node.neighbors:
            new_neigh = self.makeCopy(neigh)
            n.neighbors.append(new_neigh)

        return n
