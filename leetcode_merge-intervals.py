class Solution(object):  # O(n log n) + O(n) = O(n log n). Sorting takes over the complexity
    def merge(self, intervals):
        if len(intervals) == 0: return []
        intervals.sort(key=lambda x: int(x[0]))  # O(n log n)

        last_start, last_end = intervals[0]
        res = [[last_start, last_end]]

        for i in xrange(1, len(intervals)):  # O(n)
            start, end = intervals[i]

            if last_end >= start:
                res.pop()
                last_start, last_end = [min(start, last_start), max(end, last_end)]
                res.append([last_start, last_end])
            else:
                res.append([start, end])
                last_start, last_end = [start, end]

        return res


print Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print Solution().merge([[1, 2], [2, 3], [3, 4]])
print Solution().merge([[1, 3], [15, 18], [2, 6], [8, 10]])
