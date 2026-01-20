class Solution:  # Runtime 0 ms Beats 100%
    def findMin(self, nums: List[int]) -> int:  # Time: O(log n)
        if len(nums) == 0: return None
        
        left = 0
        right = len(nums) - 1
        mini = nums[0]

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[right]:
                return min(mini, nums[left])

            if nums[left] <= nums[mid]:
                mini = min(mini, nums[left])    
                left = mid + 1
            
            elif nums[mid] <= nums[right]:
                mini = min(mini, nums[mid])
                right = mid - 1
            
        return mini
        


print Solution().findMin([3,4,5,1,2])
print Solution().findMin([4,5,6,7,0,1,2])
print Solution().findMin([11,13,15,17])
