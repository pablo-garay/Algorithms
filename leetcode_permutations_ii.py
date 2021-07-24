from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        self.length = len(nums)
        self.permutations([], Counter(nums))
        return self.res

    def permutations(self, so_far, rest):
        if len(so_far) == self.length:
            self.res.append(so_far[:])
            return

        for item in rest.keys():
            if rest[item] == 0:
                continue
            so_far.append(item)
            rest[item] -= 1
            self.permutations(so_far, rest)
            so_far.pop()
            rest[item] += 1


print Solution().permuteUnique(nums = [1, 2, 3])
print Solution().permuteUnique(nums = [0, 1])
print Solution().permuteUnique(nums = [1])
print Solution().permuteUnique(nums = [])
print Solution().permuteUnique(nums = [6, 2, -1, 8])
print Solution().permuteUnique(nums = [1,1,2])
