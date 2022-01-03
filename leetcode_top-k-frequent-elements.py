from collections import Counter
import heapq
class Solution(object):  # Time: O(n + k log n). Space: O(n). Runtime: 80 ms, faster than 90.57%
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # O(n)

        li = [(-freq, elem) for (elem, freq) in count.iteritems()]  # O(n)
        heapq.heapify(li)  # O(n)

        res = []
        for i in xrange(k):  # O(k log n)
            res.append(heapq.heappop(li)[1])
        return res


print Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
print Solution().topKFrequent(nums = [1], k = 1)
