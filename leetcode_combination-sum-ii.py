from collections import Counter

class Solution(object):
    def combinationSum2(self, candidates, target):
        self.res = []
        count = Counter(candidates)
        self.combinations(count, target, 0, 0, [])
        return self.res

    def combinations(self, count, target, start, suma, partial):
        if suma > target:
            return
        elif suma == target:
            self.res.append(partial)
            return

        candidates = count.keys()
        for i in xrange(start, len(candidates)):
            count[candidates[i]] -= 1

            if count[candidates[i]] > 0:
                self.combinations(count, target, i, suma + candidates[i], partial + [candidates[i]])
            else:
                self.combinations(count, target, i + 1, suma + candidates[i], partial + [candidates[i]])

            count[candidates[i]] += 1


print Solution().combinationSum2(candidates = [2, 3, 6, 7], target = 7)
print Solution().combinationSum2(candidates = [2, 3, 5], target = 8)
print Solution().combinationSum2(candidates = [2], target = 1)
print Solution().combinationSum2(candidates = [1], target = 1)
print Solution().combinationSum2(candidates = [1], target = 2)
print Solution().combinationSum2(candidates = [10, 1, 2, 7, 6, 1, 5], target = 8)
print Solution().combinationSum2(candidates = [2, 5, 2, 1, 2], target = 5)
print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print Solution().combinationSum2([3,1,3,5,1,1], 8)
