class Solution(object):  # O(m + n). Optimal as we need to check each node and edge in the worst case
    def gardenNoAdj(self, N, paths):
        options = [set([1, 2, 3, 4]) for _ in xrange(N)]
        color = [None for _ in xrange(N)]
        adj = [[] for _ in xrange(N)]

        for (a, b) in paths:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        for node in xrange(N):
            color[node] = options[node].pop()

            for neigh in adj[node]:
                if not color[neigh]:
                    options[neigh].discard(color[node])

        return color



print Solution().gardenNoAdj(N = 3, paths = [[1,2],[2,3],[3,1]])
print Solution().gardenNoAdj(N = 4, paths = [[1,2],[3,4]])
print Solution().gardenNoAdj(N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
print Solution().gardenNoAdj(N = 4, paths = [])
print Solution().gardenNoAdj(N = 3, paths = [])
print Solution().gardenNoAdj(N = 3, paths = [])
