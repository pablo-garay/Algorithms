class Solution(object):  # Complexity: O(n). Optimal as we need to traverse all n elems in worst case
    def numSubarrayProductLessThanK(self, nums, k):
        start, end = (0, 0)
        total = 0
        prod = 1

        if k <= 1:
            return 0

        for end in xrange(len(nums)):
            prod *= nums[end]

            while prod >= k:
                prod /= nums[start]
                start += 1

            total += (end - start) + 1

        return total



print Solution().numSubarrayProductLessThanK(nums = [10, 5, 2, 6], k = 100)  # 8
print Solution().numSubarrayProductLessThanK(nums = [1], k = 1)  # 0
print Solution().numSubarrayProductLessThanK(nums = [1, 3, 2], k = 1)  # 0
print Solution().numSubarrayProductLessThanK(nums = [1, 3, 2], k = 7)  # 6
print Solution().numSubarrayProductLessThanK(nums = [1, 3, 2], k = 6)  # 4
print Solution().numSubarrayProductLessThanK(nums = [1, 3, 2], k = 5)  # 4
print Solution().numSubarrayProductLessThanK(nums = [3, 5, 3], k = 5)  # 2
