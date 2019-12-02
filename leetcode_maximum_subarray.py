class Solution(object):  # O(n) solution - optimal as we need to traverse all n elems in the worst case
    def maxSubArray(self, nums):
        global_max = carried = nums[0]

        for i in xrange(1, len(nums)):
            carried = max(carried + nums[i], nums[i])
            if carried > global_max:
                global_max = carried

        return global_max


print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print Solution().maxSubArray([-1])
print Solution().maxSubArray([0])
print Solution().maxSubArray([1, 0, 0, 0, 1])
