class Solution(object):  # Runtime: 462 ms, faster than 83.15%. Memory Usage: less than 93.09%
    def minSteps(self, s, t):  # Time: O(len(s) + len(t)). Space: O(1) because we use two arrays of constant size (26)
        encoded_s, encoded_t = (self.encode(s), self.encode(t))
        diff = 0

        for i in xrange(len(encoded_s)):
            diff += abs(encoded_s[i] - encoded_t[i])

        return diff

    def encode(self, word):
        encoding = [0] * 26
        for letter in word:
            encoding[ord(letter) - ord("a")] += 1
        return encoding


print Solution().minSteps(s = "leetcode", t = "coats")
print Solution().minSteps(s = "night", t = "thing")
print Solution().minSteps(s = "a", t = "b")
print Solution().minSteps(s = "ba", t = "b")
print Solution().minSteps(s = "ab", t = "b")

