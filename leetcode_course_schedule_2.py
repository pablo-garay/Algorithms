TEMP_MARK, PERM_MARK = (1, 2)

class Solution(object):  # Runtime 70 ms Beats 89.93%
    def canFinish(self, numCourses, prerequisites):  # Time: O(|v| + |e|) - optimal as need to traverse whole graph in worst case. Space: O(|v| + |e|)
        adj = {}; self.visited = {}

        for node in xrange(numCourses): adj[node] = []
        for (node1, node2) in prerequisites:
            adj[node2].append(node1)
        
        for node in xrange(numCourses):
            if node not in self.visited:
                if self.dfs(node, adj) is False:
                    return False
        return True
    
    def dfs(self, node, adj):
        self.visited[node] = TEMP_MARK

        for neigh in adj[node]:
            if neigh not in self.visited:
                if not self.dfs(neigh, adj): return False
            elif self.visited[neigh] == TEMP_MARK:
                return False
        
        self.visited[node] = PERM_MARK
        return True

      
print Solution().canFinish(2, [[1,0]] )
print Solution().canFinish(2, [[1,0],[0,1]])
