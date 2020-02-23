from collections import defaultdict

def bfs(n, dist, adj1, adj2):  # O(m + n) as each node & edge is visited a linear amount of times
    visited_1 = [False for _ in xrange(n)]
    visited_2 = [False for _ in xrange(n)]
    visited_1[0] = visited_2[0] = True
    q = [0]
    lvl = 0
    color = True

    while q:
        next_q = []
        lvl += 1
        adj = adj1 if color else adj2
        visited = visited_1 if color else visited_2

        for node in q:
            for neigh in adj[node]:
                if not visited[neigh]:
                    next_q.append(neigh)
                    visited[neigh] = True

                    if dist[neigh] < 0 or (dist[neigh] > 0 and lvl < dist[neigh]):
                        dist[neigh] = lvl

        color = not color
        q = next_q

    return dist

class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        dist = [-1 for _ in xrange(n)]
        dist[0] = 0

        adj_red = defaultdict(set)
        adj_blue = defaultdict(set)

        for (u, v) in red_edges:
            adj_red[u].add(v)

        for (u, v) in blue_edges:
            adj_blue[u].add(v)

        dist = bfs(n, dist, adj_red, adj_blue)
        dist = bfs(n, dist, adj_blue, adj_red)

        return dist


print Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[1,2]], blue_edges = [])
print Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[2,1]])
print Solution().shortestAlternatingPaths(n = 3, red_edges = [[1,0]], blue_edges = [[2,1]])
print Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[1,2]])
print Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]])

print Solution().shortestAlternatingPaths(n = 5, red_edges = [[0,1],[1,2],[2,3],[3,4]], blue_edges = [[1,2],[2,3],[3,1]])
