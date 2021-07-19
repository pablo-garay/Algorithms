import math

class Solution(object):  # O(log n) solution. Optimal as it's a binary search on a sorted array
    def searchRange(self, nums, target):
        if len(nums) == 0: return [-1, -1]

        start, end = 0, len(nums) - 1
        start = self.binSearch(nums, target, start, end, True)
        if start == -1: return [-1, -1]
        end = self.binSearch(nums, target, start, end, False)

        return [start, end]

    def binSearch(self, nums, target, start, end, left):
        while start < end:
            if left:
                mid = int(math.floor((start + end) / 2.0))
            else:
                mid = int(math.ceil((start + end) / 2.0))

            if nums[mid] == target:
                if left:
                    end = mid
                else:
                    start = mid

            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1

        if nums[start] != target:
            return -1

        return start


print Solution().searchRange(nums = [5,7,7,8,8,10], target=8)
print Solution().searchRange(nums = [5,7,7,8,8,10], target=6)
print Solution().searchRange(nums = [], target = 0)
print Solution().searchRange(nums = [8,8,8,8,8,8], target=8)

