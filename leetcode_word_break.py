class Solution(object):
    wordDict = {}
    memo = None
    string_given = ""

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.wordDict = wordDict
        self.string_given = s
        length = len(s)
        self.memo = [[None for j in xrange(length)] for i in xrange(length)]

        start, end = (0, len(s) - 1)

        for i in xrange(start, end + 1):
            # print "\nWill check " + self.string_given[start:i + 1]
            self.check(start, end)
        # print self.memo
        return self.memo[start][end]


    def check(self, start, end):
        if not self.string_given[start:end + 1]:  # string is empty
            # print "Empty string: " + self.string_given[start:end + 1]
            return True
        elif self.memo[start][end] is not None:
            # print self.string_given[start:end + 1] + " already calculated and in memo."
            return self.memo[start][end]
        elif self.string_given[start:end + 1] in self.wordDict:
            # print self.string_given[start:end + 1] + " in dictionary"
            self.memo[start][end] = True
            return True

        else:
            for i in xrange(start, end):
                if self.check(start, i) and self.check(i + 1, end):
                    self.memo[start][end] = True
                    return True

        self.memo[start][end] = False
        return False


print Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"])
print Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
print Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
