TEMP_MARK, PERM_MARK = (1, 2)

class Solution(object):  # Runtime 64 ms Beats 98.57%
    def findOrder(self, numCourses, prerequisites):  # O(m + n) as each edge and node in graph is visited at most twice
        self.adj = {}; self.visited = {}
        self.inv_topolog_order = []

        for node in xrange(numCourses): self.adj[node] = []
        for (node1, node2) in prerequisites:
            self.adj[node2].append(node1)
        
        for node in xrange(numCourses):
            if node not in self.visited:
                if not self.dfs(node): return []
        
        return reversed(self.inv_topolog_order)


    def dfs(self, node):
        self.visited[node] = TEMP_MARK

        for neigh in self.adj[node]:
            if neigh not in self.visited:
                if not self.dfs(neigh): return False
            elif self.visited[neigh] == TEMP_MARK:
                return False
        
        self.visited[node] = PERM_MARK
        self.inv_topolog_order.append(node)
        return True


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
