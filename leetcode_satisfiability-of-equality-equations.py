class Solution(object):  # Runtime: 24 ms, faster than 99.10% of Python online submissions
    def equationsPossible(self, equations):  # Time: O(|e|*inv_ackermann(|vertices|)) as we do |e| union operations ( each takes inv_ackermann(|vertices|) ). Space: O(|v|)
        def union(x, y):
            x, y = (find(x), find(y))
            if x == y: return 0
            if y < x: (x, y) = (y, x)
            parent[y] = x
            return 1

        def find(x):
            while x != parent[x]:
                x, parent[x] = (parent[x], parent[parent[x]])
            return x

        parent = {}

        for eq in equations:
            u, v = eq[0], eq[3]
            if u not in parent: parent[u] = u
            if v not in parent: parent[v] = v

            if eq[1] == "=":
                union(u, v)

        for eq in equations:
            u, v = eq[0], eq[3]

            if eq[1] == "!":
                if find(u) == find(v):
                    return False

        return True


print Solution().equationsPossible(equations = ["a==b","b!=a"])
print Solution().equationsPossible(equations = ["b==a","a==b"])
print Solution().equationsPossible(equations = ["a==b","b!=c","c==a"])