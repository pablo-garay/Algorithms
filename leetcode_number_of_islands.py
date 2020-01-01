class Solution(object):
    def get_adjacent(self, grid, row, col, num_rows, num_cols):
        grid[row][col] = '0'

        for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= r < num_rows and 0 <= c < num_cols and grid[r][c] == '1':
                self.get_adjacent(grid, r, c, num_rows, num_cols)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        for row in xrange(num_rows):
            for col in xrange(num_cols):
                if grid[row][col] == '1':
                    self.get_adjacent(grid, row, col, num_rows, num_cols)
                    num_islands += 1

        return num_islands