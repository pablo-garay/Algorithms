class Solution(object):  # Runtime 25 ms Beats 98.83%
    def findMin(self, nums):  # Each operation cuts the array in half, or at least removes two elems from consideration
        mini = nums[0]
        left, right = (0, len(nums) - 1)

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] and nums[mid] > nums[right]:
                mini = min(mini, nums[left])
                left = mid + 1

            elif nums[left] > nums[mid] and nums[mid] <= nums[right]:
                mini = min(mini, nums[mid])
                left, right = (left + 1, mid - 1)
            
            else:
                mini = min(mini, nums[left], nums[right])
                left, right = (left + 1, right - 1)
        
        return mini
