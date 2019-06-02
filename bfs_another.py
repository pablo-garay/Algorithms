from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[Li
        st[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        adj = {}
        for u,v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []

            adj[u].append(v)
            adj[v].append(u)

        results = {}
        min_height = n
        for root in xrange(n):
            parent, level, max_level = self.bfs(root, adj)

            if max_level not in results:
                results[max_level] = []
            results[max_level].append(root)
            if max_level < min_height:
                min_height = max_level

        return results[min_height]

    def bfs(self, s, adj):
        frontier = deque([s])
        parent = {s: None}
        level = {s: 0}

        while frontier:
            u = frontier.popleft()
            for v in adj[u]:
                if not v in parent:
                    parent[v] = u
                    level[v] = level[u] + 1
                    frontier.append(v)
        return parent, level


print Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
print Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
print Solution().findMinHeightTrees(1, [])
