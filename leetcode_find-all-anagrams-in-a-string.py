from collections import Counter
class Solution(object):  # Memory Usage: less than 99.75%
    def findAnagrams(self, s, p):  # Time: O(|s|) - optimal as need to traverse whole string s in worst case. Space: O(|p| + |s|)
        if len(p) > len(s): return []

        needed = Counter(p); number_zeros = 0; window_len = len(p)

        for i in xrange(window_len - 1):
            if s[i] in needed:
                needed[s[i]] -= 1
                if needed[s[i]] == 0:
                    number_zeros += 1

        left, right = (0, window_len - 1); res = []

        while right < len(s):
            # print needed, number_zeros
            if s[right] in needed:
                needed[s[right]] -= 1
                if needed[s[right]] == 0:
                    number_zeros += 1

            if number_zeros == len(needed.keys()):
                res.append(left)

            if s[left] in needed:  # return letter on left side
                if needed[s[left]] == 0:
                    number_zeros -= 1
                needed[s[left]] += 1

            left += 1; right += 1

        return res


print Solution().findAnagrams(s = "cbaebabacd", p = "abc")
print Solution().findAnagrams(s = "abab", p = "ab")
print Solution().findAnagrams(s = "d", p = "d")
print Solution().findAnagrams(s = "d", p = "e")
print Solution().findAnagrams("abaacbabc", "abc")
print Solution().findAnagrams("baa", "aa")
