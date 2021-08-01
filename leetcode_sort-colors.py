class Solution(object):  # Complexity | Time: O(n). Optimal as need to check each elem of array. Space: O(1)
    def sortColors(self, nums):
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        index = 0
        for val in xrange(len(count)):
            for i in xrange(count[val]):
                nums[index] = val
                index += 1

        return nums


print Solution().sortColors([2,0,2,1,1,0])
print Solution().sortColors([2,0,1])
print Solution().sortColors([0])
print Solution().sortColors([1])
print Solution().sortColors([2])

