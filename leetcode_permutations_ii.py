from collections import Counter

class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        self.permutations([], Counter(nums))
        return self.res

    def permutations(self, so_far, rest):
        if not rest:
            self.res.append(so_far[:])
            return

        for item in rest.keys():
            so_far.append(item)
            rest[item] -= 1
            if rest[item] == 0:
                del rest[item]
            self.permutations(so_far, rest)
            so_far.pop()
            rest[item] += 1


print Solution().permuteUnique(nums = [1, 2, 3])
print Solution().permuteUnique(nums = [0, 1])
print Solution().permuteUnique(nums = [1])
print Solution().permuteUnique(nums = [])
print Solution().permuteUnique(nums = [6, 2, -1, 8])
print Solution().permuteUnique(nums = [1,1,2])
