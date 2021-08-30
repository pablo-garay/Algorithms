def palindrome(s):  # Runtime: 588 ms, faster than 97.89% | Memory Usage: less than 99.70%
    if len(s) <= 1: return True
    a, z = (0, len(s) - 1)

    while a < z:
        if s[a] != s[z]:
            return False
        a += 1
        z -= 1
    return True

class Solution(object):
    def partition(self, s):
        self.memo = {}
        return self.check(s)

    def check(self, s):
        if s in self.memo:
            return self.memo[s]

        out = []

        if palindrome(s):
            out.append([s])

        for i in xrange(1, len(s)):
            prefix, suffix = (s[:i], s[i:])
            if palindrome(prefix):
                for li in self.check(suffix):
                    out.append([prefix] + li)

        self.memo[s] = out
        return out


print Solution().partition(s = "aab")
print Solution().partition(s = "a")

print Solution().partition(s = "aabbcc")
print Solution().partition(s = "aabbaa")
print Solution().partition(s = "abcdeffedcba")
