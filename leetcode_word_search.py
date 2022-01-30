class Solution(object):  # Runtime: 1388 ms, faster than 99.16%. Memory Usage: less than 96.95%
    def check_adjacent(self, word, curr_letter_index, pos_dict, (last_row, last_col)):
        if curr_letter_index >= len(word):
            return True

        letter = word[curr_letter_index]

        for adj_tuple in [(last_row - 1, last_col), (last_row + 1, last_col), (last_row, last_col - 1), (last_row, last_col + 1)]:
            r, c = adj_tuple

            if 0 <= r <= self.num_rows and 0 <= c <= self.num_cols:
                if adj_tuple in pos_dict[letter] and adj_tuple not in self.used:
                    self.used.add(adj_tuple)
                    if self.check_adjacent(word, curr_letter_index + 1, pos_dict, adj_tuple):
                        return True
                    self.used.remove(adj_tuple)

        return False


    def exist(self, board, word):
        pos_dict = {}
        self.num_rows, self.num_cols = len(board), len(board[0])
        self.used = set()

        if not word:  # empty string
            return True

        # init positions dict
        for r in xrange(self.num_rows):
            for c in xrange(self.num_cols):
                letter = board[r][c]
                if letter not in pos_dict:
                    pos_dict[letter] = set()
                pos_dict[letter].add((r, c))

        if set(word).difference(pos_dict.keys()):
            return False

        # start from first letter of word
        for pos_tuple in pos_dict[word[0]]:
            self.used.add(pos_tuple)
            if self.check_adjacent(word, 1, pos_dict, pos_tuple):
                return True
            self.used.remove(pos_tuple)

        return False


board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]
print Solution().exist(board, "ABCCED")
print Solution().exist(board, "SEE")
print Solution().exist(board, "ABCB")
print Solution().exist(board, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print Solution().exist(board, "X")
