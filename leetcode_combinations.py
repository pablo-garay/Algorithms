class Solution(object):
    def combine(self, n, k):
        items = [_ for _ in xrange(1, n + 1)]
        self.res = []
        self.combinations([], items, 0, 0, k)
        return self.res

    def combinations(self, partial, items, start, curr_count, k):
        if curr_count == k:
            self.res.append(partial)
            return

        for i in xrange(start, len(items)):
            self.combinations(partial + [items[i]], items, i + 1, curr_count + 1, k)


print Solution().combine(4, 2)
print Solution().combine(1, 1)
print Solution().combine(1, 0)
