class Solution(object):
    def longestCommonSubsequence(self, text1, text2):  # Time: O(mxn). Space: O(mxn)
        memo = [[0 for _ in xrange(len(text2) + 1)] for _ in xrange(len(text1) + 1)]

        for i2 in reversed(xrange(len(text2))):
            for i1 in reversed(xrange(len(text1))):
                memo[i1][i2] = max(1 + memo[i1 + 1][i2 + 1] if text1[i1] == text2[i2] else 0,
                                   memo[i1 + 1][i2],
                                   memo[i1][i2 + 1])

        return memo[0][0]


print Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
print Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc")
print Solution().longestCommonSubsequence(text1 = "abc", text2 = "def")
print Solution().longestCommonSubsequence(text1 = "abcd", text2 = "bcabcd")
print Solution().longestCommonSubsequence(text1 = "abcd", text2 = "abcdefgh")
print Solution().longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr")
print Solution().longestCommonSubsequence("aaa", "aaaaa")
print Solution().longestCommonSubsequence("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print Solution().longestCommonSubsequence("mhunuzqrkzsnidwbun", "szulspmhwpazoxijwbq")
print Solution().longestCommonSubsequence("papmretkborsrurgtina", "nsnupotstmnkfcfavaxgl")
