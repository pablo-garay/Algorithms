class Solution(object):  # Runtime: 20 ms, faster than 97.23%
    def findMin(self, nums):  # Time: O(log n) for na array elems (bin search complexity). Space: O(1)
        left, right = (0, len(nums) - 1)
        mid = (left + right) / 2

        while nums[left] > nums[right] and right - left >= 2:
            if nums[right] < nums[left] < nums[mid]:
                left, right = (mid, right)
                mid = (left + right) / 2

            if nums[mid] < nums[right] < nums[left]:
                left, right = (left, mid)
                mid = (left + right) / 2

        return min(nums[left], nums[right])


print Solution().findMin([3,4,5,1,2])
print Solution().findMin([4,5,6,7,0,1,2])
print Solution().findMin([11,13,15,17])
