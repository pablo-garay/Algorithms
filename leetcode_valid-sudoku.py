from collections import defaultdict

class Solution(object):  # Complexity: Linear. One pass. Optimal as each array item has to be visited once in worst case. Faster than 91.79 %
    def isValidSudoku(self, board):
        visited_row = defaultdict(set)
        visited_col = defaultdict(set)
        visited_subbox = defaultdict(set)

        for row in xrange(9):
            for col in xrange(9):
                if board[row][col] != ".":
                    if board[row][col] in visited_row[row]:
                        return False

                    if board[row][col] in visited_col[col]:
                        return False

                    if board[row][col] in visited_subbox[(row / 3, col / 3)]:
                        return False

                    visited_row[row].add(board[row][col])
                    visited_col[col].add(board[row][col])
                    visited_subbox[(row / 3, col / 3)].add(board[row][col])

        return True


print Solution().isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print Solution().isValidSudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
