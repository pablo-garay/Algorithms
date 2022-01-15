class Solution(object):  # Time: O(|e|*inv_ackermann(|vertices|)) as we do |e| union operations ( each takes inv_ackermann(|vertices|) ). Space: O(|v|)
    def findRedundantConnection(self, edges):
        def union(x, y):
            x, y = (find(x), find(y))
            if x == y: return 0
            if y < x: x, y = (y, x)
            parent[y] = x
            return 1

        def find(x):
            while parent[x] != x:
                x, parent[x] = (parent[x], parent[parent[x]])
            return x

        parent = {}
        for (u, v) in edges:  # O(|e|)
            parent[u] = u
            parent[v] = v

        for (u, v) in edges:  # O(|e|*inv_ackermann(|vertices|)) as we do |e| union operations ( each takes inv_ackermann(|vertices|) )
            if not union(u, v):
                out = [u, v]

        return out


print Solution().findRedundantConnection(edges = [[1,2],[1,3],[2,3]])
print Solution().findRedundantConnection(edges = [[1,2],[2,3],[3,4],[1,4],[1,5]])
print Solution().findRedundantConnection(edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]])
