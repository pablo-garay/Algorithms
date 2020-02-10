import heapq

class Solution(object):  # O(n)
    def thirdMax(self, nums):
        nums = set(nums)  # O(n)
        if len(nums) < 3: return max(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)  # O(n)

        for i in xrange(2):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

print Solution().thirdMax([3, 2, 1])
print Solution().thirdMax([1, 2])
print Solution().thirdMax([2, 2, 3, 1])
print Solution().thirdMax([2, 1])
print Solution().thirdMax([1, 1, 2])