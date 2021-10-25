class Solution(object):
    def maxSubarraySumCircular(self, nums):
        maxsum_kadane, minsum = nums[0], nums[0]
        accum_kadane, accum_from_start, cur_min = (0, 0, 0)

        for i in xrange(0, len(nums)):
            accum_kadane += nums[i]
            accum_from_start += nums[i]
            cur_min = min(cur_min + nums[i], nums[i])

            maxsum_kadane = max(maxsum_kadane, accum_kadane)
            minsum = min(minsum, cur_min)
            if accum_kadane < 0:
                accum_kadane = 0

        return max(maxsum_kadane, accum_from_start - minsum) if maxsum_kadane > 0 else maxsum_kadane


print Solution().maxSubarraySumCircular(nums = [1,-2,3,-2])
print Solution().maxSubarraySumCircular(nums = [5,-3,5])
print Solution().maxSubarraySumCircular(nums = [3,-1,2,-1])
print Solution().maxSubarraySumCircular(nums = [3,-2,2,-3])
print Solution().maxSubarraySumCircular(nums = [-2,-3,-1])
print Solution().maxSubarraySumCircular(nums = [2,-1,2])
print Solution().maxSubarraySumCircular(nums = [2,2,-1,2,2])
print Solution().maxSubarraySumCircular(nums = [2,2,-1,2,2,-100])
print Solution().maxSubarraySumCircular(nums = [2,2,2,2])
print Solution().maxSubarraySumCircular([-2,2,-2,9])
print Solution().maxSubarraySumCircular([0,5,8,-9,9,-7,3,-2])
