from collections import defaultdict

class Solution(object):  # O(m + n). Optimal as we need to check each node and edge in the worst case
    def gardenNoAdj(self, N, paths):
        options = [set([1, 2, 3, 4]) for _ in xrange(N)]
        color = [None for _ in xrange(N)]
        adj = defaultdict(list)

        for (a, b) in paths:
            a, b = (a - 1, b - 1)
            adj[a].append(b)
            adj[b].append(a)

        for node in xrange(N):
            if not color[node]:
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
