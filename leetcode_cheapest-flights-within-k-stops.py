from collections import defaultdict

class Solution(object):  # BFS. Optimal as need to traverse each node/edge at least once in worst case
    def findCheapestPrice(self, n, flights, src, dst, k):
        self.adj = defaultdict(set)
        self.cost = defaultdict(dict)
        self.best = [float('inf') for _ in xrange(n)]
        self.best[src] = 0

        for (u, v, co) in flights:
            self.adj[u].add(v)
            self.cost[u][v] = co

        self.bfs(src, k)

        if self.best[dst] == float('inf'): return -1
        return self.best[dst]

    def bfs(self, src, k):
        frontier = [(src, 0)]
        parent = {}
        stops = -1

        while frontier and stops < k:
            next_frontier = []

            for (u, prev_cost) in frontier:
                for v in self.adj[u]:
                    if v not in parent or (v in parent and prev_cost + self.cost[u][v] < self.best[v]):
                        self.best[v] = prev_cost + self.cost[u][v]
                        next_frontier.append((v, self.best[v]))
                        parent[v] = u

            frontier = next_frontier
            stops += 1


print Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)
print Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0)
print Solution().findCheapestPrice(n = 5, flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], src = 2, dst = 1, k = 1)
print "************"
print Solution().findCheapestPrice(n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1)

