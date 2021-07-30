class Solution(object):  # Linear: O(n) as each elem in array is visited only once. Optimal as need to traverse each elem once in the worst case
    def rob(self, nums):
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]

        memo1 = [0 for _ in xrange(len(nums) + 1)]
        memo2 = [0 for _ in xrange(len(nums) + 1)]

        for i in reversed(xrange(len(nums) - 1)):
            memo1[i] = max(nums[i] + memo1[i + 2], memo1[i + 1])
            memo2[i] = max(nums[i + 1] + memo2[i + 2], memo2[i + 1])

        return max(memo1[0], memo2[0])


print Solution().rob(nums = [2,3,2])  # 3
print Solution().rob(nums = [1,2,3,1])  # 4
print Solution().rob(nums = [0])  # 0
print Solution().rob(nums = [2,7,9,3,1])  # 11
print Solution().rob(nums = [1,2,20,1])  # 21
print Solution().rob(nums = [1,2,20,1,1]) # 21
print Solution().rob(nums = [1,20,1,1]) # 21
print Solution().rob(nums = [1,2,20,1,2]) # 22
print Solution().rob(nums = [3,2,20,1,1]) # 23
print Solution().rob(nums = [1,2,0,1,100]) # 102
print Solution().rob([2,1,1,1]) # 3
