class Solution(object):
    def combinationSum3(self, k, n):
        self.res = []
        self.combinations(range(1, 9 + 1), n, 0, 0, [], k)
        return self.res

    def combinations(self, candidates, target, start, suma, partial, k):
        if suma > target:
            return

        if len(partial) == k:
            if suma == target:
                self.res.append(partial)
            return

        for i in xrange(start, len(candidates)):
            self.combinations(candidates, target, i + 1, suma + candidates[i], partial + [candidates[i]], k)


print Solution().combinationSum3(k = 3, n = 7)
print Solution().combinationSum3(k = 3, n = 9)
print Solution().combinationSum3(k = 4, n = 1)
print Solution().combinationSum3(k = 3, n = 2)
print Solution().combinationSum3(k = 9, n = 45)
