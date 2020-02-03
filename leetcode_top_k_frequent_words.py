from collections import Counter, defaultdict
import heapq, bisect

class Solution(object):  # Complexity: # O(n log n)
    def topKFrequent(self, words, k):
        li = []
        freq_dict = defaultdict(list)
        count = Counter(words)  # O(n)

        for elem, freq in count.iteritems():  # O(n log n)
            bisect.insort(freq_dict[freq], elem)  # log(n)
            li.append(-freq)

        for key in freq_dict:  # Need to reverse order so that behavior is as if "popleft". Complexity: O(n)
            freq_dict[key].reverse()

        heapq.heapify(li)  # O(n)

        top_k = []
        for i in xrange(k):  # O(k log n)
            next_max_freq = -heapq.heappop(li)    # O(log n)
            top_k.append(freq_dict[next_max_freq].pop())

        return top_k



print Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2)
print Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)
