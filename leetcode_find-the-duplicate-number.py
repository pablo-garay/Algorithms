class Solution(object):  # Linear time and constant space complexity (two passes at most)
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


print Solution().findDuplicate(nums = [1,3,4,2,2])
print Solution().findDuplicate(nums = [3,1,3,4,2])
print Solution().findDuplicate(nums = [1,1])
print Solution().findDuplicate(nums = [1,1,2])

