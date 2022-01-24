class Solution(object):  # Time: O(n ALPHA(n)). To perform a sequence of m addition, union, or find operations on a disjoint-set forest with n nodes requires total time O(m ALPHA(n)), where ALPHA(n) is the extremely slow-growing inverse Ackermann function
    def findCircleNum(self, isConnected):  # Space: O(n). # Runtime: 148 ms, faster than 98.00%
        def union(x, y):
            x, y = (find(x), find(y))
            if x == y: return 0
            parent[x] = parent[y] = min(x, y)
            return 1

        def find(x):
            while parent[x] != x:  # path splitting
                x, parent[x] = (parent[x], parent[parent[x]])
            return x

        num_nodes = num_provinces = len(isConnected)
        parent = [num for num in xrange(num_nodes)]

        for node1 in xrange(num_nodes):
            for node2 in xrange(node1 + 1, num_nodes):
                if isConnected[node1][node2]:
                    num_provinces -= union(node1, node2)

        return num_provinces


print Solution().findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]])
print Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]])
print Solution().findCircleNum(isConnected = [[1]])
print Solution().findCircleNum(isConnected = [[1, 0], [0, 1]])
print Solution().findCircleNum(isConnected = [[1, 1], [1, 1]])
print Solution().findCircleNum(isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]])
