class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0 or k % len(nums) == 0:
            print nums
            return

        index = (len(nums) - k) % len(nums)
        output = []
        indices = []

        for i in xrange(len(nums)):
            output.append(nums[(index + i) % len(nums)])
            indices.append((index + i) % len(nums))

        print output



Solution().rotate([1,2,3,4,5,6,7], 4)
Solution().rotate([1,2,3,4,5,6,7], 3)
Solution().rotate([1,2,3,4,5,6,7], 2)
Solution().rotate([1,2,3,4,5,6,7], 1)
Solution().rotate([1,2,3,4,5,6,7], 0)
Solution().rotate([1,2,3,4,5,6,7], 7)
Solution().rotate([1,2,3,4,5,6,7], 14)
Solution().rotate([1,2,3,4,5,6,7], 56)
Solution().rotate([-1,-100,3,99], k=2)
Solution().rotate([-1,-100,3,99], k=0)
