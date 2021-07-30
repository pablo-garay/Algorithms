class Solution(object):  # Linear: O(n) as each elem in array is visited only once. Optimal as need to traverse each elem once in the worst case
    def rob(self, nums):
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]

        memo = [0 for _ in xrange(len(nums))]

        memo[-1] = nums[-1]
        memo[-2] = max(nums[-2], nums[-1])

        for i in reversed(xrange(len(nums) - 2)):
            memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])

        return memo[0]


print Solution().rob(nums = [1,2,3,1])
print Solution().rob(nums = [2,7,9,3,1])
