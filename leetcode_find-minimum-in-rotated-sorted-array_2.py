class Solution(object):  # Runtime 23 ms Beats 82.82%
    def findMin(self, nums):  # Time: O(log n)
        mini = nums[0]
        left, right = (0, len(nums) - 1)

        while left <= right:
            if nums[left] <= nums[right]:
                return min(mini, nums[left])
            
            mid = (left + right) // 2

            if nums[left] <= nums[mid] and nums[mid] > nums[right]:
                left = mid + 1

            elif nums[left] > nums[mid] and nums[mid] <= nums[right]:
                left, right = (left + 1, mid)
        
        return mini


print Solution().findMin([3,4,5,1,2])
print Solution().findMin([4,5,6,7,0,1,2])
print Solution().findMin([11,13,15,17])
