class Solution(object):  # Complexity O(n). Optimal as we need to traverse each array elem at least once in worst case
    def twoSum(self, nums, target):
        dict = {}
        for pos in xrange(len(nums)):
            num = nums[pos]
            if num not in dict:
                dict[num] = []
            dict[num].append(pos)

            if target - num in dict:
                if target - num == num:
                    if len(dict[num]) >= 2:
                        return [dict[num][0], dict[num][1]]
                else:
                    return [dict[target - num][0], pos]

        return []


print Solution().twoSum([2, 7, 11, 15], 9)
print Solution().twoSum([2, 7, 5, 5], 10)
print Solution().twoSum([2, 7, 5, 5], 100)
print Solution().twoSum([1], 1)
print Solution().twoSum([1, 0], 1)
print Solution().twoSum([], 1)
