class Solution(object):
    def palindrome(self, word):
        a, z = (0, len(word) - 1)

        while a < z:
            if word[a] != word[z]:
                return False
            a += 1
            z -= 1
        return True


    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        out = []

        dict = {}
        for n in xrange(len(words)):
            word = words[n]
            if word not in dict:
                dict[word] = []
            dict[word].append(n)

        for pos in xrange(len(words)):
            word = words[pos]

            for i in xrange(1, len(word) + 1):
                prefix, suffix = word[:i], word[i:]
                r_prefix, r_suffix = prefix[::-1], suffix[::-1]
                # print r_prefix
                # print "prefix: %s, suffix: %s" %(prefix, suffix)

                if not suffix and prefix == r_prefix and "" in dict:  # special corner case when empty string
                    for pos2 in dict[""]:
                        out.append([pos, pos2])

                if r_prefix in dict and self.palindrome(suffix):
                    for pos2 in dict[r_prefix]:
                        if pos != pos2:
                            out.append([pos, pos2])

                if r_suffix in dict and self.palindrome(prefix):
                    for pos2 in dict[r_suffix]:
                        if pos2 != pos:
                            out.append([pos2, pos])

        return out



print Solution().palindromePairs( ["gab", "cat", "bag", "alpha"])
print Solution().palindromePairs( ["gab", "cat", "bag", "alpha", "nurses", "race", "car", "run", "nu", "aba"] )
print Solution().palindromePairs( ["gab", "cat", "bag", "alpha", "gab"])
print Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])
print Solution().palindromePairs(["bat","tab","cat"])
print Solution().palindromePairs(["a","a","b", "ba", "a"])
print Solution().palindromePairs(["a","a","b", "ba", "a", "c", "a"])
print Solution().palindromePairs(["", ""])
print Solution().palindromePairs(["", "a"])
print Solution().palindromePairs(["a", ""])
print Solution().palindromePairs(["a","b","c","ab","ac","aa"])
