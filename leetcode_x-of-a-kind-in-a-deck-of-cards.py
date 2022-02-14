from collections import Counter

def gcd(a, b):
    while b: a, b = b, a % b
    return a

class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = Counter(deck)
        g = min(count.values())

        for val in count.values():  # O(n * log(min(count.values()))) ~ O(n)
            g = gcd(g, val)

        return g > 1


print Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1])
print Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3])
print Solution().hasGroupsSizeX([1, 2])
