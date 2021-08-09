from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        count, black = Counter(), set()

        for char in s:
            count[char] += 1
            if count[char] < k:
                black.add(char)
            else:
                black.discard(char)

        left, right = 0, len(s) - 1

        if len(black) == 0:
            return right - left + 1

        return max([self.longestSubstring(subs, k) for subs in s.split(black.pop())])


print Solution().longestSubstring(s = "aaabb", k = 3)
print Solution().longestSubstring(s = "ababbc", k = 2)
print Solution().longestSubstring("ababacb", 3)
print Solution().longestSubstring("bbaaacddcaabdbd", 3)



