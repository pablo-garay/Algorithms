class Solution(object):
    def findFarmland(self, land):  # Time: O(m x n). Space: O(m x n)
        self.rows, self.cols = (len(land), len(land[0]))
        out = []

        self.tag = {}; tag_num = 1
        for r in xrange(self.rows):  # O(m x n) : each elem in matrix will be visited at most once
            for c in xrange(self.cols):
                if land[r][c] == 1 and (r, c) not in self.tag:
                    self.first = self.second = (r, c)
                    self.dfs(land, r, c, tag_num)
                    out.append(self.first + self.second)

        return out

    def dfs(self, land, r, c, tag_num):
        self.tag[(r, c)] = tag_num

        for (r2, c2) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= r2 < self.rows and 0 <= c2 < self.cols and land[r2][c2] == 1 and (r2, c2) not in self.tag:
                self.second = max(self.second, (r2, c2))
                self.dfs(land, r2, c2, tag_num)


print Solution().findFarmland(
land = [[1,0,0],[0,1,1],[0,1,1]]
)
print Solution().findFarmland(
land = [[1,1],[1,1]]
)
print Solution().findFarmland(
land = [[0]]
)

