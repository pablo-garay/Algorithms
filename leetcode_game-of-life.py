# Encoding:
# Prev:0, New:0 = 2 00
# Prev:0, New:1 = 2 01
# Prev:1, New:0 = 2 10
# Prev:1, New:1 = 2 11

class Solution(object):  # O(1) space. O(mn) time - two passes. Runtime: 8 ms, faster than 99.79%
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])

        for r in xrange(rows):
            for c in xrange(cols):
                life = 0
                for r2, c2 in [(r - 1, c - 1), (r-1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
                    if 0 <= r2 < rows and 0 <= c2 < cols and board[r2][c2] in (1, 210, 211):
                        life += 1

                if board[r][c] in (1, 210, 211):
                    if life < 2 or life > 3:
                        board[r][c] = 210
                    else:
                        board[r][c] = 211

                if board[r][c] in (0, 200, 201):
                    if life == 3:
                        board[r][c] = 201
                    else:
                        board[r][c] = 200

        for r in xrange(rows):
            for c in xrange(cols):
                if board[r][c] == 200 or board[r][c] == 210: board[r][c] = 0
                if board[r][c] == 201 or board[r][c] == 211: board[r][c] = 1

        # print board


Solution().gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
Solution().gameOfLife(board = [[1,1],[1,0]])
Solution().gameOfLife([[0,1,0],
                             [0,0,1],
                             [1,1,1],
                             [0,0,0]])
Solution().gameOfLife(board = [[1,1],[1,0]])
Solution().gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]) == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
