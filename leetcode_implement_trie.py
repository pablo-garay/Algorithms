class Node():
    def __init__(self):
        self.dict = {}
        self.word_end = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root

        for char in word:
            if char not in node.dict:
                node.dict[char] = Node()
            node = node.dict[char]

        node.word_end = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root

        for char in word:
            if char not in node.dict:
                return False
            node = node.dict[char]

        if node.word_end:
            return True
        return False


    def startsWith(self, word):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root

        for char in word:
            if char not in node.dict:
                return False
            node = node.dict[char]

        return True


trie = Trie()
trie.insert("apple")
print trie.search("apple")      # returns true
print trie.search("app")        # returns false
print trie.startsWith("app")    # returns true
print trie.startsWith("apd")    # returns false
trie.insert("app")
print trie.search("app")        # returns true
print trie.search("")           # returns false
print trie.startsWith("a")      # returns true
print trie.startsWith("b")      # returns false
print trie.startsWith("bpple")  # returns false
