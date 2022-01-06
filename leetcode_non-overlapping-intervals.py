class Solution(object):
    def eraseOverlapIntervals(self, intervals):  # Time: O(n log n) - complexity is dominated by sorting. Space: O(1) - less than 95.46%
        intervals.sort(key=lambda x: (x[1], x[0]))  # O(n log n) | Fundamental to sort by end of interval
        num = 0

        left, right = intervals[0]
        next = 1
        while next < len(intervals):  # O(n)
            (left2, right2) = intervals[next]
            if left2 < right <= right2:
                num += 1
            else:
                left, right = left2, right2
            next += 1

        return num


print Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]])
print Solution().eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]])
print Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3]])
print Solution().eraseOverlapIntervals(intervals = [[2,3],[1,3]])