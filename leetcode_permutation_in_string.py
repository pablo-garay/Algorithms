from collections import Counter

class Solution(object):  # Time: Linear O(len(s1) + len(s2). Space: Linear O(len(s1))
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False

        needed = Counter(s1)
        needed_count = len(s1)
        start, end = (0, len(s1))

        for i in xrange(end):
            if s2[i] in needed:
                needed[s2[i]] -= 1
                if needed[s2[i]] >= 0: needed_count -= 1

        while end <= len(s2):
            if needed_count == 0:
                return True

            if s2[start] in needed:
                needed[s2[start]] += 1
                if needed[s2[start]] > 0: needed_count += 1

            if end <= len(s2) - 1 and s2[end] in needed:
                needed[s2[end]] -= 1
                if needed[s2[end]] >= 0: needed_count -= 1

            start, end = (start + 1, end + 1)

        return False


print Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo")
print Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo")
print Solution().checkInclusion(s1 = "abc", s2 = "eidboaoo")
print Solution().checkInclusion(s1 = "abcd", s2 = "eidboaoo")
print Solution().checkInclusion(s1 = "abcd", s2 = "abcd")
print Solution().checkInclusion(s1 = "eidboaoo", s2 = "abcd")
print Solution().checkInclusion(s1 = "abcde", s2 = "abcd")
print Solution().checkInclusion(s1 = "dcba", s2 = "abcd")
print Solution().checkInclusion(s1 = "dinitrophenylhydrazine", s2 = "acetylphenylhydrazine")
print Solution().checkInclusion("adc", "dcda")
print Solution().checkInclusion("abc","cccccbabbbaaaa")
print Solution().checkInclusion("abcdxabcde", "abcdeabcdx")

