class Solution(object):  # Exponential with exponent equal to length of input string. O(4^n) where n is length of input string
    mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        if len(digits) == 0: return []
        self.res = []
        self.accum = ""
        self.backtrack(digits, 0)
        return self.res

    def backtrack(self, digits, i):
        if i >= len(digits):
            self.res.append(self.accum)
            return

        for letter in self.mapping[int(digits[i])]:
            self.accum += letter
            self.backtrack(digits, i + 1)
            self.accum = self.accum[:-1]

    def letterCombinationsIterativeVersion(self, digits):
        if len(digits) == 0: return []
        res = []
        stack = [(0, "")]

        while stack:
            (next_i, accum) = stack.pop()

            if next_i >= len(digits):
                res.append(accum)
                continue

            for letter in self.mapping[int(digits[next_i])]:
                stack.append((next_i + 1, accum + letter))

        return res




print Solution().letterCombinations(digits = "23")
print Solution().letterCombinations(digits = "")
print Solution().letterCombinations(digits = "2")
print Solution().letterCombinations(digits = "999")
print Solution().letterCombinations(digits = "9946")
print Solution().letterCombinations(digits = "77777")
