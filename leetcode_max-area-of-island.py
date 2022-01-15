class Solution(object):  # Runtime: 104 ms, faster than 96.88%
    def maxAreaOfIsland(self, grid):  # Time: O(mxn) - optimal as need to traverse whole matrix in worst case. Space: O(1)
        rows, cols = (len(grid), len(grid[0]))
        res = 0

        for r in xrange(rows):
            for c in xrange(cols):
                if grid[r][c] == 1:
                    val = self.dfs(grid, r, c, rows, cols)
                    res = max(res, val)
        return res

    def dfs(self, grid, r, c, rows, cols):
        val = 1
        grid[r][c] = 0  # if can't rewrite matrix, make copy at the beginning

        for (r2, c2) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # adjacent
            if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == 1:
                val += self.dfs(grid, r2, c2, rows, cols)

        return val


print Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]])
print Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])