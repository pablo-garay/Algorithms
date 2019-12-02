class Solution(object):
    def minSubArrayLen(self, s, nums):
        start, end = (0, 0)
        curr_sum, res = 0, len(nums) + 1

        for end in xrange(len(nums)):
            curr_sum += nums[end]

            while curr_sum >= s and start <= end:
                if (end - start + 1) < res:
                    res = end - start + 1

                curr_sum -= nums[start]
                start += 1

        if res == len(nums) + 1:
            res = 0
        return res


print Solution().minSubArrayLen(s = 7, nums = [2,3,1,2,4,3])
print Solution().minSubArrayLen(s = 7, nums = [2,8,1,2,4,3])
print Solution().minSubArrayLen(s = 777, nums = [2,8,1,2,4,3])
