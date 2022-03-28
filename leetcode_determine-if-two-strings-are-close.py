from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):  # Time: O(len(word1) + O(len(word2))). Space: O(1) - we keep count of max 26 chars so it's bounded
        if len(word1) != len(word2): return False

        chars1 = Counter(word1); chars2 = Counter(word2)
        count_repetitions = Counter()

        for char in chars1:
            if char not in chars2: return False
            count_repetitions[chars1[char]] += 1

        for char in chars2:
            if char not in chars1: return False
            count_repetitions[chars2[char]] -= 1
            if count_repetitions[chars2[char]] == 0: del count_repetitions[chars2[char]]

        if not count_repetitions:
            return True

        return False


print Solution().closeStrings(word1 = "abc", word2 = "bca")
print Solution().closeStrings(word1 = "a", word2 = "aa")
print Solution().closeStrings(word1 = "cabbba", word2 = "abbccc")
print Solution().closeStrings(word1 = "cabbba", word2 = "cabbbd")
print Solution().closeStrings(word1 = "aaabba", word2 = "aaabbb")
