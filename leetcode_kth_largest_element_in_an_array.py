import heapq

class Solution(object):  # O(n + k log n)
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)  # O(n)

        for i in xrange(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)


print Solution().findKthLargest([3,2,1,5,6,4], k = 2)
print Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k = 4)
