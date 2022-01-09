from collections import defaultdict
class Solution:
    def validTree(self, n, edges):  # Time: O(|v| + |e|) - optimal as need to traverse whole graph in worst case. Space: O(|e|)
        self.parent = {}

        adj = defaultdict(set)
        for (u, v) in edges:  # O(|e|)
            adj[u].add(v)
            adj[v].add(u)

        if not self.dfs(0, adj):  # O(|v| + |e|)
            return False  # cycle was found
        if len(self.parent) != n - 1:
            return False  # for tree, it must be that all nodes except root have one parent node

        return True

    def dfs(self, orig, adj):
        for dest in adj[orig]:
            if dest not in self.parent:
                self.parent[dest] = orig
                adj[dest].remove(orig)  # remove same edge but in opposite direction

                if not self.dfs(dest, adj):
                    return False
            else:
                return False  # cycle in graph

        return True


print Solution().validTree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]])
print Solution().validTree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
print Solution().validTree(7, [[0,1],[0,2],[0,3],[1,4]])
print Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]])
