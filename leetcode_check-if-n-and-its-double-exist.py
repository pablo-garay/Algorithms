from collections import Counter
class Solution(object):  # Runtime: 32 ms, faster than 95.08%
    def checkIfExist(self, arr):  # Time: O(n). Space: O(n) | Obviously space can be enhanced, also make only one pass
        c = Counter(arr)
        for num in arr:
            if num == 0:
                if c[0] >= 2: return True
            else:
                if num * 2 in c: return True
        return False
