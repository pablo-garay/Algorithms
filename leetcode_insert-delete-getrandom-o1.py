from random import randint


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ds:
            ret = False
        else:
            ret = True

        self.ds.add(val)
        return ret

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.ds:
            ret = True
        else:
            ret = False

        self.ds.discard(val)
        return ret

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randind = randint(0, len(self.ds) - 1)
        return list(self.ds)[randind]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()