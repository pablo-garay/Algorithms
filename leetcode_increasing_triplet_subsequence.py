class Solution(object):  # O(n) time complexity - as n elements are visited just once - and O(1) space
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        beat_first, beat_second = nums[0], None

        for num in nums[1:]:
            if num < beat_first:
                beat_first = num
            elif num > beat_first:
                if beat_second is None:
                    beat_second = num
                elif num > beat_second:
                    return True
                elif num < beat_second:
                    beat_second = num

        return False



print Solution().increasingTriplet([1,2,3,4,5])
print Solution().increasingTriplet([5,4,3,2,1])
print Solution().increasingTriplet([1, 3, 5])
print Solution().increasingTriplet([1, 2])
print Solution().increasingTriplet([])
print Solution().increasingTriplet([2,1,5,0,3])

