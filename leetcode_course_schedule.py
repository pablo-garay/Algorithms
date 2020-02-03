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


    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in xrange(numCourses)]
        visited = [NOT_VISITED for _ in xrange(numCourses)]
        self.has_cycle = False

        for (orig, dest) in prerequisites:
            adj[orig].append(dest)

        for node in xrange(numCourses):
            if visited[node] == NOT_VISITED:
                self.dfs(node, adj, visited)

                if self.has_cycle:
                    return False
        return True


print Solution().canFinish(2, [[1,0]] )
print Solution().canFinish(2, [[1,0],[0,1]])

