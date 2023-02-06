class Solution(object):  # O(n)
    def numDecodings(self, s):
        if s == "" or s[0] == "0": return 0
        memo = [None for i in xrange(len(s) + 2)]
        memo[len(s)] = 1; memo[len(s) + 1] = 0
        
        for i in reversed(xrange(len(s))):  # O(n)
            if s[i] == "1":
                memo[i] = memo[i + 1] + memo[i + 2]
            elif s[i] == "2":
                memo[i] = memo[i + 1] + (memo[i + 2] if i + 1 < len(s) and 0 <= int(s[i + 1]) <= 6 else 0)
            elif s[i] == "0":
                memo[i] = 0
            else:
                if i + 1 < len(s) and s[i + 1] == "0": return 0  # two 0's or digit>=3 followed by 0
                memo[i] = memo[i + 1]
        
        return memo[0]



print Solution().numDecodings("1")
print Solution().numDecodings("12")
print Solution().numDecodings("226")
print Solution().numDecodings("2612")
print Solution().numDecodings("612")
print Solution().numDecodings("22612")
print Solution().numDecodings("0")
print Solution().numDecodings("022612")
print Solution().numDecodings("0022612")
print Solution().numDecodings("10022612")
print Solution().numDecodings("1022612")
print Solution().numDecodings("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
