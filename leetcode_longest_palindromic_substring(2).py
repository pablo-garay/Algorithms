class Solution(object):  # Borrowed solution. Time: O(n^2). Space: O(1)
    def longestPalindrome(self, s):
        res = ""
        for i in xrange(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome. Left, right are the middle indexes. From inner to outer
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = (left - 1, right + 1)
        return s[left + 1:right]  # there was one extra iteration (exclude left and right)


print Solution().longestPalindrome("babad")
print Solution().longestPalindrome("cbbd")
print Solution().longestPalindrome("a")
