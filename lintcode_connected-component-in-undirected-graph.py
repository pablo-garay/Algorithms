"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

from collections import defaultdict
class Solution:  # Time cost: 285ms, 98.00% beat percent
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        self.adj = defaultdict(set); self.id = defaultdict(list)
        self.visited = set(); li_nodes = []

        for node in nodes:  # O(|v| + |e|)
            for node2 in node.neighbors:
                self.adj[node.label].add(node2.label)
            li_nodes.append(node.label)

        num_connected_comp = 0
        for node in li_nodes:  # O(|v| + |e|)
            if node not in self.visited:
                num_connected_comp += 1
                self.dfs(node, num_connected_comp)

        res = [sorted(self.id[i]) for i in self.id.keys()]  # O(|v|log|v|)
        return res

    def dfs(self, orig, num_connected_comp):
        self.id[num_connected_comp].append(orig)
        self.visited.add(orig)

        for dest in self.adj[orig]:
            if dest not in self.visited:
                self.dfs(dest, num_connected_comp)
