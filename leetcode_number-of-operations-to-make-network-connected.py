from collections import defaultdict  # Runtime: 452 ms, faster than 85.99%

class Solution(object):  # Time: O(|v| + |e|) - each vertex visited at most once. Optimal as need to traverse whole graph in worse case. Space: # O(|v| + |e|)
    def makeConnected(self, n, edges):
        self.visited = set()
        self.adj = defaultdict(set)
        num_edges = num_connected_comp = 0

        for (u, v) in edges:  # O(|e|)
            self.adj[u].add(v)
            self.adj[v].add(u)
            num_edges += 1

        for node in xrange(n):  # O(|v| + |e|)
            if node not in self.visited:
                num_connected_comp += 1
                self.dfs(node)

        # print "num_connected_comp, num_edges", num_connected_comp, num_edges
        return (num_connected_comp - 1) if num_edges >= (n - 1) else -1

    def dfs(self, orig):
        self.visited.add(orig)

        for dest in self.adj[orig]:
            if dest not in self.visited:
                self.visited.add(dest)
                self.dfs(dest)


print Solution().makeConnected(4, [[0,1],[0,2],[1,2]])
print Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]])
print Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2]])
