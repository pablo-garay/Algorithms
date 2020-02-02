class Solution(object):  # O(logn * n^2)
    # *A + B > C
    # *B + C > A (satisfied when sorted)
    # *A + C > B (satisfied when sorted)

    def triangleNumber(self, nums):  # O(n^2)
        if len(nums) < 3:
            return 0

        nums.sort()  # O(nlogn)
        count = 0

        for c in reversed(xrange(2, len(nums))):
            a, b = (0, c - 1)

            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    count += b - a
                    b -= 1
                else:
                    a += 1

        return count


print Solution().triangleNumber([2,2,3,4])
print Solution().triangleNumber([48,66,61,46,94,75])
