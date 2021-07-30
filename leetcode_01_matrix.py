class Solution(object):
    def updateMatrix(self, matrix):
        if len(matrix) == 0:
            return []
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        res = [[None for c in xrange(n_cols)] for r in xrange(n_rows)]

        frontier = []
        for row in xrange(n_rows):
            for col in xrange(n_cols):
                if matrix[row][col] == 0:
                    res[row][col] = 0
                    frontier.append((row, col))

        level = 1
        while frontier:
            next_frontier = []
            for row, col in frontier:
                for r,c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if 0 <= r < n_rows and 0 <= c < n_cols:
                        if res[r][c] is None:
                            res[r][c] = level
                            next_frontier.append((r, c))
            frontier = next_frontier
            level += 1

        return res

print Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]])
print Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])
print Solution().updateMatrix([[0,0,1,0,1,1,1,0,1,1],
                               [1,1,1,1,0,1,1,1,1,1],
                               [1,1,1,1,1,0,0,0,1,1],
                               [1,0,1,0,1,1,1,0,1,1],
                               [0,0,1,1,1,0,1,1,1,1],
                               [1,0,1,1,1,1,1,1,1,1],
                               [1,1,1,1,0,1,0,1,0,1],
                               [0,1,0,0,0,1,0,0,1,1],
                               [1,1,1,0,1,1,0,1,0,1],
                               [1,0,1,1,1,0,1,1,1,0]])
