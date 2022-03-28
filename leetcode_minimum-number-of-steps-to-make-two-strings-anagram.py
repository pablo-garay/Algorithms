class Solution(object):
    def minSteps(self, s, t):  # Time: O(len(s) + len(t)). Space: O(1) because we use two arrays of constant size (26)
        encoded_s, encoded_t = (self.encode(s), self.encode(t))
        diff = 0

        for i in xrange(len(encoded_s)):
            temp = encoded_s[i] - encoded_t[i]
            if temp > 0: diff += temp

        return diff

    def encode(self, word):
        encoding = [0] * 26
        for letter in word:
            encoding[ord(letter) - ord("a")] += 1
        return encoding


# print Solution().minSteps(s = "leetcode", t = "coats")
# print Solution().minSteps(s = "night", t = "thing")
# print Solution().minSteps(s = "a", t = "b")
# print Solution().minSteps(s = "ba", t = "b")
# print Solution().minSteps(s = "ab", t = "b")
print Solution().minSteps(s = "bab", t = "aba")
print Solution().minSteps(s = "leetcode", t = "practice")
print Solution().minSteps(s = "anagram", t = "mangaar")

