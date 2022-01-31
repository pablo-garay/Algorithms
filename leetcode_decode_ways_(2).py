MAX_CHAR_VAL = 26
class Solution(object):  # Runtime: 18 ms, faster than 83.39%
    def numDecodings(self, s):  # Time: O(n) - optimal as need to traverse whole string in worst case. Space: O(n)
        memo = [None for _ in xrange(len(s) + 1)]
        memo[len(s)] = 1

        for i in reversed(xrange(len(s))):  # Time: O(n)
            if s[i] == "0":
                memo[i] = 0
            elif i < len(s) - 1 and int(s[i:i + 2]) <= MAX_CHAR_VAL:
                if s[i + 1] != "0":
                    memo[i] = memo[i + 1] + memo[i + 2]
                else:
                    memo[i] = memo[i + 2]
            else:
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
