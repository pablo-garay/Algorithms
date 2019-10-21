class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1

        # print nums
        self.reverse(nums, 0, end - k)
        # print nums
        self.reverse(nums, end - k + 1, end)
        # print nums
        self.reverse(nums, 0, end)
        # print nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1



# Solution().rotate([1,2,3,4,5,6,7], 4)
# Solution().rotate([1,2,3,4,5,6,7,8,9,10], 4)