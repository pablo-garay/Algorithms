class Solution(object):  # Runtime: 3348 ms, faster than 75.31%
    def countSubIslands(self, grid1, grid2):  # Time: O(m x n). Space: O(m x n)
        global parent; parent = {}
        self.rows, self.cols = (len(grid2), len(grid2[0]))
        self.tag = {}

        out = 0; tag_num = 0
        for r in xrange(self.rows):  # O(m x n) : each elem in grid2 will be visited at most once
            for c in xrange(self.cols):
                if (r, c) not in self.tag and grid2[r][c] == 1 and grid1[r][c] == 1:
                    tag_num += 1; self.subIsland = True
                    self.tag[(r, c)] = tag_num
                    self.dfs(grid1, grid2, r, c, tag_num)
                    if self.subIsland: out += 1

        return out

    def dfs(self, grid1, grid2, r, c, tag_num):
        for (r2, c2) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= r2 < self.rows and 0 <= c2 < self.cols and grid2[r2][c2] == 1 and (r2, c2) not in self.tag:
                if grid1[r2][c2] != 1: self.subIsland = False
                self.tag[(r2, c2)] = tag_num
                self.dfs(grid1, grid2, r2, c2, tag_num)

        return True


print Solution().countSubIslands(
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
)
print Solution().countSubIslands(
grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
)





