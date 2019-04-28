class Solution(object):
    MAX_CHAR_VAL = 26

    def numDecodings(self, s):  # O(n)
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0  # starts with 0: no way to decode
        # we add 2 extra elements to array which should be init'ed to 1 for correct computation
        memo = [None for i in xrange(len(s) + 2)]
        memo[len(s) + 1] = memo[len(s)] = 1

        # iterative DP
        for pos in reversed(xrange(0, len(s))):
            if s[pos] == '0':
                memo[pos] = 0
                if pos - 1 >= 0 and s[pos - 1] == '0':  # special case: two or more 0's in seq: no decode way
                    return 0
            else:
                if s[pos] == '*':
                    memo[pos] = 9 * memo[pos + 1]

                    if pos + 1 < len(s):
                        if s[pos + 1] == '*':
                            memo[pos] += 15 * memo[pos + 2]
                        elif '0' <= s[pos + 1] <= '6':
                            memo[pos] += 2 * memo[pos + 2]
                        else:
                            memo[pos] += memo[pos + 2]
                else:
                    memo[pos] = memo[pos + 1]
                    if pos + 1 < len(s) and s[pos + 1] == '*':
                        if s[pos] == '1':
                            memo[pos] += 9 * memo[pos + 2]
                        elif s[pos] == '2':
                            memo[pos] += 6 * memo[pos + 2]
                    elif 10 <= int(s[pos:pos + 2]) <= self.MAX_CHAR_VAL:
                        memo[pos] += memo[pos + 2]

        return memo[0] % (10 ** 9 + 7)  # first element has the solution


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
print Solution().numDecodings("*")
print Solution().numDecodings("1*")
print Solution().numDecodings("2*")
print Solution().numDecodings("**")
print Solution().numDecodings("*1")
