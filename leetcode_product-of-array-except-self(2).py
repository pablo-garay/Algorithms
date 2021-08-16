class Solution(object):  # O(n) time, O(1) space. Optimal as need to traverse each elem in array in worst case. Runtime: 196 ms, faster than 97.72 %
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        left = right = 1

        for i in xrange(len(nums)):
            ans[i] *= left
            ans[-1 - i] *= right

            left *= nums[i]
            right *= nums[-1 - i]

        return ans


print Solution().productExceptSelf(nums = [1,2,3,4])
print Solution().productExceptSelf(nums = [-1,1,0,-3,3])
print Solution().productExceptSelf(nums = [-1,0,1,-3,3])
print Solution().productExceptSelf(nums = [-1,1,0,-3,0])
