class Solution(object):  # Linear: O(n) as each elem in array is visited only once. Optimal as need to traverse each elem once in the worst case
    def rob(self, nums):
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]

        memo = dict()
        memo[len(nums) + 1] = memo[len(nums)] = 0

        for i in reversed(xrange(len(nums))):
            memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])

        i, maxi = (0, memo[0])
        while i < len(nums) - 2:
            if maxi == memo[i + 1]:
                i = i + 1
            else:
                print str(i) + " -> " + str(i + 2)
                maxi -= nums[i]
                i = i + 2

        return memo[0]


print Solution().rob(nums = [1,2,3,1])
print Solution().rob(nums = [2,7,9,3,1])
print Solution().rob(nums = [0,2,7,9,3,1])
print Solution().rob(nums = [2,7,9,100,1])
print Solution().rob(nums = [])
print Solution().rob(nums = [1])
