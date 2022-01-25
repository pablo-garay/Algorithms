class Solution(object):  # Time: O(n) - optimal as we need to traverse all the n elems of list in the worst case. Space: O(1)
    def maxProduct(self, nums):
        if len(nums) == 1: return nums[0]
        global_max = 0
        mini = maxi = 1

        for num in nums:
            if num == 0:
                mini = maxi = 1
                continue

            a = mini * num; b = maxi * num
            mini = min(a, b, num); maxi = max(a, b, num)

            global_max = max(global_max, maxi)

        return global_max

