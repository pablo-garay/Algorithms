from collections import Counter, defaultdict  # Runtime 35 ms Beats 91.96%
from heapq import *
from bisect import insort_left

class Solution(object):
    def topKFrequent(self, words, k):
        dictio, counts_list = defaultdict(list), []
        wc = Counter(words)  # O(n)

        for word, count in wc.iteritems():
            rcount = -count  # inverse for max_heap
            if rcount not in dictio: counts_list.append(rcount)
            insort_left(dictio[rcount], word)
        
        heapify(counts_list)  # O(n)

        out = []
        while len(out) < k:  # O(k log n)
            count = heappop(counts_list)  # O(log n)
            out += dictio[count][:k - len(out)]
        
        return out



print Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2)
print Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)        

