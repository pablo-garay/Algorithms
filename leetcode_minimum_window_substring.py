from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        start, end = (0, 0)
        needed = Counter(t)
        total_needed = len(t)
        ans_start, ans_end = (-1, -1)
        ans_len = len(s) + 1

        for end in xrange(len(s)):
            if s[end] in needed:
                if needed[s[end]] > 0:
                    total_needed -= 1
                needed[s[end]] -= 1

                while total_needed == 0 and start <= end:
                    if (end - start + 1) < ans_len:
                        ans_len = end - start + 1
                        ans_start, ans_end = start, end

                    if s[start] in needed:
                        needed[s[start]] += 1

                        if needed[s[start]] > 0:
                            total_needed += 1
                    start += 1

        return s[ans_start:ans_end + 1]


print Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
print Solution().minWindow(s = "ADOBECODEBANC", t = "N")
print Solution().minWindow(s = "ADOBECODEBANC", t = "C")
print Solution().minWindow(s = "ADOBECODEBANCO", t = "O")
print Solution().minWindow(s = "aaaaaaa", t = "a")
print Solution().minWindow(s = "aaaaaaab", t = "a")





