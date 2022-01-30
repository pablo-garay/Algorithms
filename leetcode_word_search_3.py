class Solution(object):  # Backtracking algorithm
    def exist(self, board, word):
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if board[r][c] == word[0]:
                    if self.search(r, c, set(), word, 0, board):
                        return True

        return False

    def search(self, r, c, visited, word, ind, board):
        if board[r][c] != word[ind]:
            return False

        if ind == len(word) - 1:
            return True

        visited.add((r, c))
        for (r2, c2) in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= r2 < len(board) and 0 <= c2 < len(board[0]) and (r2, c2) not in visited:
                if self.search(r2, c2, visited, word, ind + 1, board):
                    return True
        visited.remove((r, c))

        return False


print Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
print Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
print Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
print Solution().exist([["a"]], "a")
