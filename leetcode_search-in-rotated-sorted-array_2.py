class Solution(object):
    def search(self, nums, target):  # Time: O(log n). Space: O(1)
        left, right = (0, len(nums) - 1)

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] and nums[left] <= target <= nums[mid]:
                if nums[mid] == target: return mid
                right = mid - 1

            elif nums[mid] <= nums[right] and nums[mid] <= target <= nums[right]:
                if nums[mid] == target: return mid
                left = mid + 1

            elif nums[left] > nums[mid] and (target >= nums[left] or target <= nums[mid]):
                if nums[mid] == target: return mid
                right = mid - 1

            elif nums[mid] > nums[right] and (target >= nums[mid] or target <= nums[right]):
                if nums[mid] == target: return mid
                left = mid + 1
            
            else:
                return -1

        return -1


print Solution().search(nums = [4,5,6,7,0,1,2], target = 0)
print Solution().search(nums = [4,5,6,7,0,1,2], target = 3)
print Solution().search(nums = [1], target = 0)
print Solution().search(nums = [1], target = 1)
print Solution().search([3,1], 3)
