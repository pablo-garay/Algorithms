class Solution(object):
    def explore(self, board, row, col, row_limit, col_limit):
        board[row][col] = 'P'

        for r, c in [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]:
            if 0 <= r <= row_limit and 0 <= c <= col_limit and board[r][c] == 'O':
                self.explore(board, r, c, row_limit, col_limit)


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return
        max_row, max_col = len(board), len(board[0])

        for row in (0, max_row - 1):
            for col in xrange(max_col):
                if board[row][col] == 'O':
                    self.explore(board, row, col, max_row - 1, max_col - 1)

        for col in (0, max_col - 1):
            for row in xrange(1, max_row - 1):
                if board[row][col] == 'O':
                    self.explore(board, row, col, max_row - 1, max_col - 1)

        for row in xrange(max_row):
            for col in xrange(max_col):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'P':
                    board[row][col] = 'O'

        for line in board:
            print line
        print




Solution().solve(
    [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'X']]
)

Solution().solve(
    [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'X', 'X', 'X']]
)

Solution().solve(
    [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'O', 'X', 'X']]
)

Solution().solve(
    [['O']]
)

Solution().solve(
    [['O', 'X', 'O'],
     ['X', 'O', 'X'],
     ['O', 'X', 'O']]
)

Solution().solve([])
