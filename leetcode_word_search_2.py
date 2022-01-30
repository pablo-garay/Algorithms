from collections import defaultdict
class Solution(object):  # Runtime: 1436 ms, faster than 99.11%. Memory Usage: less than 95.63%
    def exist(self, board, word):
        pos = defaultdict(set)

        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                pos[board[r][c]].add((r, c))

        if set(word).difference(pos.keys()):
            return False

        for (r, c) in pos[word[0]]:
            if self.search(word, 0, pos, r, c, []):
                return True
        return False

    def search(self, word, ind, pos, r, c, stack):
        if ind == len(word) - 1: return True
        pos[word[ind]].remove((r, c))

        for (r2, c2) in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
            if (r2, c2) in pos[word[ind + 1]] and self.search(word, ind + 1, pos, r2, c2, stack + [(r2, c2)]):
                return True

        pos[word[ind]].add((r, c))

        return False


print Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
print Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
print Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
print Solution().exist([["a"]], "a")
print Solution().exist([["a","a","A","a"],["a","a","a","A"],["a","A","a","a"]], "AaaAaaAaa")
