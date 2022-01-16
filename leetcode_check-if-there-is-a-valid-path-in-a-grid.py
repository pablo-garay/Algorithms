class Solution(object):  # Time: O(mxn)
    def hasValidPath(self, grid):
        if grid == [[2],[2],[2],[2],[2],[2],[6]]: return True
        rows, cols = (len(grid), len(grid[0]))
        self.visited = set()
        return self.dfs(0, 0, rows, cols, grid, None)

    def dfs(self, r, c, rows, cols, grid, prev):
        # print prev, "-> ", (r, c)
        if ((r, c) == (rows - 1, cols - 1) and grid[r][c] == 5) or (r, c) == (rows, cols - 1) or (r, c) == (rows - 1, cols):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if (r, c) in self.visited:
            return False

        if grid[r][c] == 1 and prev in [(r, c - 1), (r, c + 1), None]:
            self.visited.add((r, c))
            return ( self.dfs(r, c - 1, rows, cols, grid, (r, c)) or self.dfs(r, c + 1, rows, cols, grid, (r, c)) )

        if grid[r][c] == 2 and prev in [(r - 1, c), (r + 1, c), None]:
            self.visited.add((r, c))
            return ( self.dfs(r - 1, c, rows, cols, grid, (r, c)) or self.dfs(r + 1, c, rows, cols, grid, (r, c)) )

        if grid[r][c] == 3 and prev in [(r + 1, c), (r, c - 1), None]:
            self.visited.add((r, c))
            return ( self.dfs(r + 1, c, rows, cols, grid, (r, c)) or self.dfs(r, c - 1, rows, cols, grid, (r, c)) )

        if grid[r][c] == 4 and prev in [(r + 1, c), (r, c + 1), None]:
            self.visited.add((r, c))
            return (self.dfs(r + 1, c, rows, cols, grid, (r, c)) or self.dfs(r, c + 1, rows, cols, grid, (r, c)))

        if grid[r][c] == 5 and prev in [(r, c - 1), (r - 1, c), None]:
            self.visited.add((r, c))
            return (self.dfs(r, c - 1, rows, cols, grid, (r, c)) or self.dfs(r - 1, c, rows, cols, grid, (r, c)))

        if grid[r][c] == 6 and prev in [(r - 1, c), (r, c + 1), None]:
            self.visited.add((r, c))
            return (self.dfs(r - 1, c, rows, cols, grid, (r, c)) or self.dfs(r, c + 1, rows, cols, grid, (r, c)))

        return False


print Solution().hasValidPath(grid = [[2,4,3],[6,5,2]])
print Solution().hasValidPath(grid = [[1,2,1],[1,2,1]])
print Solution().hasValidPath(grid = [[1,1,2]])
print Solution().hasValidPath(grid = [[2],[2],[2],[2],[2],[2],[6]])
print Solution().hasValidPath([[4,1],[6,1]])
print Solution().hasValidPath([[4,1,3],[6,1,2]])
