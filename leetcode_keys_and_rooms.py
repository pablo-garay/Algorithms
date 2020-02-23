def dfs(node, adj, unvisited):  # O(|N| + |E|) as each node & edge is visited at most once
    unvisited.remove(node)

    for neigh in adj[node]:
        if neigh in unvisited:
            dfs(neigh, adj, unvisited)

class Solution(object):
    def canVisitAllRooms(self, adj):
        unvisited = set(xrange(len(adj)))
        dfs(0, adj, unvisited)

        return not bool(len(unvisited))


print Solution().canVisitAllRooms([[1],[2],[3],[]])
print Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
print Solution().canVisitAllRooms([[]])
print Solution().canVisitAllRooms([[], []])
print Solution().canVisitAllRooms([[1], []])
print Solution().canVisitAllRooms([[0], []])
