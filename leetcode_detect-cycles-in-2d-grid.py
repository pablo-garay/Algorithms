class Solution(object):  # Time: O(m x n) - optimal as need to traverse whole matrix in worst case (no elem visited more than twice at most).
    def containsCycle(self, grid):  # Space: O(m x n)
        rows, cols = len(grid), len(grid[0])
        self.visited = set()

        for r in xrange(rows):
            for c in xrange(cols):
                if (r, c) not in self.visited:
                    if self.dfs(grid, r, c, None, None, rows, cols):
                        return True
        return False

    def dfs(self, grid, r, c, last_r, last_c, rows, cols):
        if (r, c) in self.visited:
            return True

        self.visited.add((r, c))

        for (r2, c2) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= r2 < rows and 0 <= c2 < cols:
                if grid[r2][c2] == grid[r][c] and (r2, c2) != (last_r, last_c):
                    if self.dfs(grid, r2, c2, r, c, rows, cols):
                        return True

        return False


print Solution().containsCycle(grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]])
print Solution().containsCycle(grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]])
print Solution().containsCycle(grid = [["a","b","b"],["b","z","b"],["b","b","a"]])
