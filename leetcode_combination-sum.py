class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.combinations(candidates, target, 0, 0, [])
        return self.res

    def combinations(self, candidates, target, start, suma, partial):
        if suma > target:
            return
        elif suma == target:
            self.res.append(partial)
            return

        for i in xrange(start, len(candidates)):
            self.combinations(candidates, target, i, suma + candidates[i], partial + [candidates[i]])


print Solution().combinationSum(candidates = [2,3,6,7], target = 7)
print Solution().combinationSum(candidates = [2,3,5], target = 8)
print Solution().combinationSum(candidates = [2], target = 1)
print Solution().combinationSum(candidates = [1], target = 1)
print Solution().combinationSum(candidates = [1], target = 2)
