from collections import defaultdict
class Solution(object):
    def countSubIslands(self, grid1, grid2):  # Time: O(m x n * inv ack(m x n)) | Space: O(m x n) - Memory Usage: less than 88.27%
        def union(x, y):
            x, y = (find(x), find(y))
            if x == y: return 0
            parent[x] = parent[y] = min(x, y)
            return 1

        def find(x):
            while x != parent[x]:
                x, parent[x] = (parent[x], parent[parent[x]])
            return x

        parent = {}
        self.rows, self.cols = (len(grid2), len(grid2[0]))

        for r in xrange(self.rows):  # O(m x n)
            for c in xrange(self.cols):
                if grid2[r][c] == 1: parent[(r, c)] = (r, c)

        for r in xrange(self.rows):  # O(m x n) * O(inv ack(m x n))
            for c in xrange(self.cols):
                if grid2[r][c] == 1:
                    for (r2, c2) in [(r - 1, c), (r, c - 1)]:
                        if 0 <= r2 < self.rows and 0 <= c2 < self.cols and grid2[r2][c2] == 1:
                            union((r, c), (r2, c2))

        islands = defaultdict(list)
        for key, val in parent.iteritems():  # O(m x n)
            islands[find(val)].append(key)

        out = 0
        for island in islands.values():  # O(m x n)
            subIsland = True
            for (r, c) in island:
                if grid1[r][c] != 1:
                    subIsland = False
                    break
            if subIsland: out += 1
        return out


print Solution().countSubIslands(
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
)
print Solution().countSubIslands(
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
)

