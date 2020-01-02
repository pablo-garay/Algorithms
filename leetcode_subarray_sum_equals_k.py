from collections import Counter

class Solution(object):  # Complexity: O(n) with 2 passes on n elems
    def subarraySum(self, nums, k):
        num_subarrays = 0
        dict = Counter()
        tot_sum = 0

        for i in xrange(len(nums)):
            tot_sum += nums[i]
            dict[tot_sum] += 1

        offset = 0
        for i in xrange(len(nums)):
            num_subarrays += dict[k + offset]
            offset += nums[i]
            dict[offset] -= 1

        return num_subarrays



print Solution().subarraySum(nums = [1,1,1], k = 2)
print Solution().subarraySum(nums = [1,1,1, -1], k = 1)
print Solution().subarraySum(nums = [1, 2, 3, 4, 5, 6], k = 3)
print Solution().subarraySum(nums = [1, 2, 3, 4, 5, 6], k = 1)
print Solution().subarraySum(nums = [1], k = 1)
print Solution().subarraySum(nums = [1, 2], k = 2)
