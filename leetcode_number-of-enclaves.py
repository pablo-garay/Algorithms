class Solution(object):  # Time: O(mxn) - optimal as need to traverse whole matrix in worst case. Space: O(1)
    def numEnclaves(self, grid):
        rows, cols = (len(grid), len(grid[0]))
        res = 0

        for r in xrange(rows):
            for c in xrange(cols):
                if grid[r][c] == 1:
                    val = self.dfs(grid, r, c, rows, cols)
                    if val > 0: res += val
        return res

    def dfs(self, grid, r, c, rows, cols):
        val = 1
        grid[r][c] = 0  # if can't rewrite matrix, make copy at the beginning

        for (r2, c2) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:  # adjacent
            if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == 1:
                val2 = self.dfs(grid, r2, c2, rows, cols)
                if val2 < 0:
                    val = val2
                elif val2 > 0 and val > 0:
                    val += val2

        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            val = -1

        return val


print Solution().numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print Solution().numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
print Solution().numEnclaves(grid = [[1]])
print Solution().numEnclaves(grid = [[0]])
print Solution().numEnclaves(grid = [[0,0,0,0,0],
                                     [0,1,1,1,0],
                                     [0,1,0,1,0],
                                     [0,1,1,1,0],
                                     [0,0,0,0,0]])
