class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0: return -1
        left, right = (0, len(nums) - 1)

        if nums[left] <= nums[right]:
            return next(res for res in [self.bin_search(nums, target, left, right), -1] if res is not None)

        mid = self.find_mid(nums, left, right)
        return next(res for res in [self.bin_search(nums, target, left, mid), self.bin_search(nums, target, mid + 1, right), -1]  if res is not None)

    def find_mid(self, nums, left, right):
        mid = left

        while left != right:
            mid = (left + right) / 2

            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return mid

    def bin_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) / 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None


print Solution().search(nums = [4,5,6,7,0,1,2], target = 0)
print Solution().search(nums = [4,5,6,7,0,1,2], target = 3)
print Solution().search(nums = [1], target = 0)
print Solution().search(nums = [1], target = 1)
print Solution().search([3,1], 3)

