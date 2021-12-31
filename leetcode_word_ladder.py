class Solution(object):
    @staticmethod
    def adjacent(word1, word2):
        diff = 0
        for i in xrange(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1:
                    return False

        return True

    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        q = [beginWord]
        length = 1

        while q:
            length += 1
            new_q = []

            for node in q:
                for w in wordList.copy():
                    if self.adjacent(node, w):
                        wordList.remove(w)  # mark visited

                        if w == endWord:
                            return length
                        new_q.append(w)
            q = new_q

        return 0
