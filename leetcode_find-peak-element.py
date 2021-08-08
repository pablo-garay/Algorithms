class Solution(object):  # O(log n) solution (binary search)
    def findPeakElement(self, nums):
        if len(nums) == 1: return 0

        left, right = (0, len(nums) - 1)

        if nums[left] > nums[left + 1]: return left
        if nums[right] > nums[right - 1]: return right

        while left <= right:
            mid = (left + right) / 2

            if nums[mid - 1] <= nums[mid] >= nums[mid + 1]:
                return mid

            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid + 1

            elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
                right = mid - 1

            elif nums[left] > nums[right]:
                right = mid - 1

            else:
                left = mid + 1

        return -1

print Solution().findPeakElement(nums = [1,2,3,1])
print Solution().findPeakElement(nums = [1,2,1,3,5,6,4])
print Solution().findPeakElement(nums = [1,2,1,3,6,5,4])
print Solution().findPeakElement(nums = [1,2])
print Solution().findPeakElement(nums = [2, 1])
print Solution().findPeakElement(nums = [1])
