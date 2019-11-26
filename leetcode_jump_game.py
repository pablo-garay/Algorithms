class Solution(object):  # Optimal O(n) solution
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in reversed(xrange(len(nums) - 1)):
            if i + nums[i] >= goal:
                goal = i

        return (goal == 0)


print Solution().canJump([2,3,1,1,4])
print Solution().canJump([3,2,1,0,4])
# print Solution().canJump([])
print Solution().canJump([0])
print Solution().canJump([0, 0])
print Solution().canJump([0, 1])
print Solution().canJump([1, 0])
