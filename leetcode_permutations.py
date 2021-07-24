class Solution(object):
    def permute(self, nums):
        self.res = []
        self.permutations([], set(nums))
        return self.res

    def permutations(self, so_far, rest):
        if not rest:
            self.res.append(list(so_far))
            return

        for item in list(rest):
            so_far.append(item)
            rest.remove(item)
            self.permutations(so_far, rest)
            so_far.pop()
            rest.add(item)


print Solution().permute(nums = [1,2,3])
print Solution().permute(nums = [0,1])
print Solution().permute(nums = [1])
print Solution().permute(nums = [])
print Solution().permute(nums = [6,2,-1,8])
