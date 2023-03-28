
# //You are given an undirected tree with N nodes numbered from 0 to N-1 and an array A[] where A[i] denotes the value assigned to i-th node. The connections between the nodes are provided in a 2-dimensional array edges[]. The task is to find the maximum path sum between any two nodes. (Both the nodes can be the same also). Note: The path sum is equal to the sum of the value of the nodes of that path.

# // Example 1:
# // Input: N = 6, A[] = [4, -1, -3, 5, 7, -2],  
# // edges[][] = [[1, 2], [0, 3, 4, 5], [0], [1], [1], [1]]
# // Output: 11
# // Explanation: The Simple path sum between node 3 and 4 through node 1. i.e., 5-1+7 = 11

# function addEdge(adj, s, d) {
#   adj[s].push(d)
#   adj[d].push(s)
# }

# function findMaximumPathSum() {
#   return 0
# }

# const N = 6
# const A = [4, -1, -3, 5, 7, -2]

# var adj = []
# for (let i = 0; i < N; i++) {
#     adj.push([])
# }

# addEdge(adj, 0, 1)
# addEdge(adj, 0, 2)
# addEdge(adj, 1, 3)
# addEdge(adj, 1, 4)
# addEdge(adj, 1, 5)

# console.log(findMaximumPathSum())

from collections import defaultdict

# class Solution():
#     def findMaximumPathSum(self, values=None, edges=None):
#         if len(edges) == 0: return 0
#         self.maxi = float("-inf")
#         self.val = values
#         self.adj = defaultdict(list)

#         for i in xrange(len(edges)):
#             neighs_list = edges[i]
#             self.adj[i] = neighs_list

#         for node in xrange(len(edges)):
#             self.visited = set()
#             self.dfs(node, self.val[node])

#         # print self.adj
#         return self.maxi

#     def dfs(self, node, accum):
#         self.maxi = max(self.maxi, accum)
#         self.visited.add(node)

#         for neigh in self.adj[node]:
#             if neigh not in self.visited:
#                 self.dfs(neigh, accum + self.val[neigh])


class Solution():  # Time: O(m + n) for n nodes with m edges
    def findMaximumPathSum(self, values=None, edges=None):
        if len(edges) == 0: return 0
        maxi = values[0]

        opt = values
        local_max = values[:]
        adj = defaultdict(list)

        for i in xrange(len(edges)):
            neighs_list = edges[i]
            for j in neighs_list:
                if j > i:
                    adj[i].append(j)
        # print adj

        for node_num in reversed(xrange(len(values))):
            curr_val = opt[node_num]
            for neigh in adj[node_num]:
                if curr_val + opt[neigh] > opt[node_num]:
                    opt[node_num] = curr_val + opt[neigh]
                if opt[neigh] > 0:
                    local_max[node_num] += opt[neigh]
                # opt[node_num] = max(curr_val, )
                maxi = max(maxi, opt[node_num], local_max[node_num])

            # print node_num, opt, maxi

        return maxi






print Solution().findMaximumPathSum(values=[4, -1, -3, 5, 7, -2], edges=[[1, 2], [0, 3, 4, 5], [0], [1], [1], [1]])



values=[4, -1, -3, 5, 7, -2]
edges=[[1, 2], [0, 3, 4, 5], [0], [1], [1], [1]]

# -1 - 2 - 2 - -3
# n * O(m + n)


