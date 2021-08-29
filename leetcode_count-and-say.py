class Solution(object):  # 24 ms, faster than 95.10% | memory usage beats 97.88%
    def parse(self, s):
        new_s = ""
        prev, count = (s[0], 1)

        for i in xrange(1, len(s)):
            if s[i] == prev:
                count += 1
            else:
                new_s += str(count) + prev
                prev, count = (s[i], 1)
        new_s += str(count) + prev  # last

        return new_s

    def countAndSay(self, n):
        s = "1"
        for i in xrange(2, n + 1):
            s = self.parse(s)

        return s


print Solution().countAndSay(1)
print Solution().countAndSay(2)
print Solution().countAndSay(3)
print Solution().countAndSay(4)
print Solution().countAndSay(5)
print Solution().countAndSay(6)
print Solution().countAndSay(7)
print Solution().countAndSay(8)
print Solution().countAndSay(9)
print Solution().countAndSay(10)
print Solution().countAndSay(11)
print Solution().countAndSay(12)
print Solution().countAndSay(13)
print Solution().countAndSay(14)
print Solution().countAndSay(15)
print Solution().countAndSay(16)
print Solution().countAndSay(17)
print Solution().countAndSay(18)
print Solution().countAndSay(19)
print Solution().countAndSay(20)
