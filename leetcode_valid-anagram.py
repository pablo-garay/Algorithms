from collections import Counter
class Solution(object):  # Memory Usage: less than 99.61%
    def isAnagram(self, s, t):  # Time: O(m) where m is length of strings - optimal as need to traverse whole strings in worst case. Space: O(m)
        if len(s) != len(t): return False
        count = Counter(s); matched = 0

        for letter in t:
            if letter not in count:
                return False
            else:
                count[letter] -= 1
                if count[letter] >= 0:
                    matched += 1

        if matched == len(s) == len(t):
            return True

        return False


print Solution().isAnagram(s = "anagram", t = "nagaram")
print Solution().isAnagram(s = "anagramm", t = "nagaram")
print Solution().isAnagram(s = "anagram", t = "nagaramm")
print Solution().isAnagram(s = "rat", t = "car")
