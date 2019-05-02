from collections import Counter
import heapq

class MaxHeap:
    @staticmethod
    def heapify(x):
        heapq.heapify(x)

    @staticmethod
    def heappop(x):
        return -heapq.heappop(x)

    @staticmethod
    def heappush(heap, item):
        heapq.heappush(heap, -item)

    @staticmethod
    def heapget(x):
        return [-elem for elem in x]

    @staticmethod
    def highest(x):
        return -x[0]


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []

        curr_window = Counter(nums[:k - 1])
        max_heap = [-elem for elem in nums[:k - 1]]
        MaxHeap.heapify(max_heap)
        # print MaxHeap.heapget(max_heap)
        last_pos = 0

        for n in nums[k - 1:]:
            curr_window[n] += 1
            MaxHeap.heappush(max_heap, n)
            max_window = MaxHeap.highest(max_heap)
            while max_window not in curr_window:
                MaxHeap.heappop(max_heap)
                max_window = MaxHeap.highest(max_heap)
                # print max_window

            output.append(max_window)

            curr_window[nums[last_pos]] -= 1  # item's not anymore in window
            if curr_window[nums[last_pos]] == 0:
                del curr_window[nums[last_pos]]  # remove item from dictionary if no more of this item in window
            last_pos += 1

        return output


print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
