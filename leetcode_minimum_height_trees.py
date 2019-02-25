from collections import Counter

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        degrees = Counter()
        leaves = set()
        max_degree = 0
        num_nodes = n

        if n == 1:
            return [0]

        adj = [[] for _ in xrange(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

            if degrees[u] == 1: leaves.add(u)
            elif u in leaves: leaves.remove(u)

            if degrees[v] == 1: leaves.add(v)
            elif v in leaves: leaves.remove(v)

            if degrees[u] > max_degree: max_degree = degrees[u]
            if degrees[v] > max_degree: max_degree = degrees[v]

        removed_nodes = set()
        while num_nodes > 2:
            next_level = set()
            for u in leaves:
                num_nodes -= 1
                removed_nodes.add(u)

                for v in adj[u]:
                    if v not in removed_nodes:
                        degrees[v] -= 1
                        if degrees[v] <= 1:
                            next_level.add(v)
            leaves = next_level

        return list(leaves)


print Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])
print Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
print Solution().findMinHeightTrees(1, [])
print Solution().findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
