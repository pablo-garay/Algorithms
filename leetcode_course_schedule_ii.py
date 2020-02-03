NOT_VISITED, TEMP_MARK, PERM_MARK = (0, 1, 2)

class Solution(object):  # O(m + n) as each edge and node in graph is visited at most twice
    def dfs(self, node, adj, visited):
        visited[node] = TEMP_MARK

        for adjac in adj[node]:
            if visited[adjac] == NOT_VISITED:
                self.dfs(adjac, adj, visited)
            elif visited[adjac] == TEMP_MARK:
                self.has_cycle = True

        visited[node] = PERM_MARK
        self.topolog_order.append(node)


    def findOrder(self, numCourses, prerequisites):
        adj = [[] for _ in xrange(numCourses)]
        visited = [NOT_VISITED for _ in xrange(numCourses)]
        self.topolog_order = []
        self.has_cycle = False

        for (orig, dest) in prerequisites:
            adj[orig].append(dest)

        for node in xrange(numCourses):
            if visited[node] == NOT_VISITED:
                self.dfs(node, adj, visited)

                if self.has_cycle:
                    return []

        return self.topolog_order


print Solution().findOrder(2, [[1, 0]])
print Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
print Solution().findOrder(4, [[1,0],[0,1], [1, 0], [2, 0], [3, 1], [3, 2]])
print Solution().findOrder(4, [])
print Solution().findOrder(0, [])
print Solution().findOrder(1, [])
print Solution().findOrder(3, [(0, 1)])

print Solution().findOrder(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]])
print Solution().findOrder(3, [[0, 1], [2, 0]])
print Solution().findOrder(3, [[2, 0], [0, 1]])
print Solution().findOrder(3, [[2, 0], [1, 0]])
