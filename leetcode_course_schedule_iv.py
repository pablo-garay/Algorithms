from collections import defaultdict

class Solution(object):  # We run a DFS (linear time) starting from each node at most once. Optimal as need to visit each node/edge in worst case
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        self.visited = defaultdict(set)
        adj = [[] for _ in xrange(numCourses)]
        out = []

        for (orig, dest) in prerequisites:
            adj[orig].append(dest)

        for (source, dest) in queries:
            if source not in self.visited:
                self.dfs(adj, source, source, dest)

            if dest in self.visited[source]:
                out.append(True)
            else:
                out.append(False)

        return out

    def dfs(self, adj, source, curr, dest):
        if curr in self.visited:
            self.visited[source] = self.visited[source].union(self.visited[curr])  # re-use previous result/already visited node
            return

        self.visited[source].add(curr)

        for neigh in adj[curr]:
            if neigh not in self.visited[source]:
                self.dfs(adj, source, neigh, dest)


print Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])
print Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]])
print Solution().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
