from collections import Counter
from heapq import *

class Solution(object):  # Runtime 73 ms Beats 95.22%
    def topKFrequent(self, nums, k):  # Time: O(n + k log n). Space: O(n)
        count = Counter(nums)  # O(n)

        li = [(-count, elem) for (elem, count) in count.iteritems()]  # O(n)
        heapify(li)  # O(n)
        
        out = [heappop(li)[1] for i in xrange(k)]  # O(k log n)
        return out
