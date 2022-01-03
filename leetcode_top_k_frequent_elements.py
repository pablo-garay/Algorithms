from collections import Counter, defaultdict
import heapq

class Solution(object):  # Complexity: # O(n + k log n)
    def topKFrequent(self, nums, k):
        li = []
        freq_dict = defaultdict(list)
        count = Counter(nums)  # O(n)

        for elem, freq in count.iteritems():  # O(n)
            freq_dict[freq].append(elem)
            li.append(-freq)

        heapq.heapify(li)  # O(n)

        top_k = []
        for i in xrange(k):  # O(k log n)
            next_max_freq = -heapq.heappop(li)    # O(log n)
            top_k.append(freq_dict[next_max_freq].pop())

        return top_k


print Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
print Solution().topKFrequent(nums = [1,1,1,2,2,3,3,3], k = 2)
print Solution().topKFrequent(nums = [1,1,1,2,2,3,3,3,3], k = 1)
print Solution().topKFrequent(nums = [1], k = 1)
print Solution().topKFrequent(nums = [], k = 0)
