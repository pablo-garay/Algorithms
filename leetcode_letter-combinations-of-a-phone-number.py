class Solution(object):  # Exponential with exponent equal to length of input string. O(4^n) where n is length of input string
    mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        if len(digits) == 0: return []
        self.res = []
        self.accum = ""
        self.dfs(digits, 0)
        return self.res

    def dfs(self, digits, i):
        if i >= len(digits):
            self.res.append(self.accum)
            return

        for letter in self.mapping[int(digits[i])]:
            self.accum += letter
            self.dfs(digits, i + 1)
            self.accum = self.accum[:-1]


print Solution().letterCombinations(digits = "23")
print Solution().letterCombinations(digits = "")
print Solution().letterCombinations(digits = "2")
print Solution().letterCombinations(digits = "999")
print Solution().letterCombinations(digits = "9946")
print Solution().letterCombinations(digits = "77777")
