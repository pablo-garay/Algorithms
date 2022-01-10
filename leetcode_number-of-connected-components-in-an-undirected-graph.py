from collections import defaultdict
class Solution:
    def countComponents(self, n, edges):  # Time: O(|v| + |e|) - each vertex visited at most once. Optimal as need to traverse whole graph in worse case
        self.visited = set()
        self.adj = defaultdict(set)
        num_connected_comp = 0

        for (u, v) in edges:  # O(|e|)
            self.adj[u].add(v)
            self.adj[v].add(u)

        for node in xrange(n):  # O(|v| + |e|)
            if node not in self.visited:
                num_connected_comp += 1
                self.dfs(node)

        return num_connected_comp

    def dfs(self, orig):
        self.visited.add(orig)

        for dest in self.adj[orig]:
            if dest not in self.visited:
                self.visited.add(dest)
                self.dfs(dest)


print Solution().countComponents(n = 5, edges = [[0,1],[1,2],[3,4]])
print Solution().countComponents(n = 5, edges = [[0,1],[1,2],[2,3],[3,4]])
