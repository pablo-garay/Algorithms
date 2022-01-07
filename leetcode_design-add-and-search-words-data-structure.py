class WordDictionary(object):  # Runtime: 281 ms, faster than 87.84%. Memory Usage: less than 88.40%
    def __init__(self):
        self.dic = {}

    def addWord(self, word):  # O(len|word|)
        dic = self.dic
        for char in word:
            if char not in dic: dic[char] = {}
            dic = dic[char]
        dic[None] = None

    def search(self, word):  # O(len|word|) if word contains no "." . Otherwise O(num English letters in word + 27^num(".")) in worst case (i.e. we have big dictionary with many words)
        return self.search2(word, 0, self.dic)

    def search2(self, word, index, dic):
        if index == len(word):
            if None in dic:
                return True
            return False

        if word[index] == ".":
            for key in dic.keys():
                if key and self.search2(word, index + 1, dic[key]):
                    return True

        elif word[index] in dic:
            return self.search2(word, index + 1, dic[word[index]])

        return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
# param_2 = obj.search(word)