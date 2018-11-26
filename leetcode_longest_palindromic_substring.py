class Solution(object):
    memo = None

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        self.memo = [[None for col in xrange(len(s))] for row in xrange(len(s))]

        window = len_s - 1
        while window >= 0:
            i = 0
            while i + window <= len_s - 1:
                # print i, i + window
                if self.checkPalindromic(s, i, i + window):
                    return s[i:i + window + 1]
                i += 1
            window -= 1

        longest = ""
        return longest

    def checkPalindromic(self, s, i, j):
        if i > j:
            return True

        if self.memo[i][j] is None:
            if i == j:
                self.memo[i][i] = True
            else:
                if s[i] == s[j] and self.checkPalindromic(s, i + 1, j - 1):
                    self.memo[i][j] = True
                else:
                    self.memo[i][j] = False

        # print self.memo
        return self.memo[i][j]


print Solution().longestPalindrome("babad")
print Solution().longestPalindrome("cbbd")
print Solution().longestPalindrome("a")
