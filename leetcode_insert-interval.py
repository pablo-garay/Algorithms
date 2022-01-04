from bisect import *

class Solution(object):  # Time: O(n) where n is num of intervals - optimal as need to move all intervals in worst case. Space: O(1) - other than n-lenghted output
    def insert(self, intervals, newInterval):  # Runtime: 56 ms, faster than 91.58%
        pos = bisect_left(intervals, newInterval)  # O (log n)
        left, right = (pos - 1, pos)
        mini, maxi = (newInterval[0], newInterval[1])

        while left >= 0 and newInterval[0] <= intervals[left][1]:  # O(n/2)
            mini = min(mini, intervals[left][0])
            maxi = max(maxi, intervals[left][1])
            left -= 1

        while right < len(intervals) and newInterval[1] >= intervals[right][0]:  # O(n/2)
            mini = min(mini, intervals[right][0])
            maxi = max(maxi, intervals[right][1])
            right += 1

        return intervals[:left + 1] + [[mini, maxi]] + intervals[right:]  # O(n)


print Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
print Solution().insert(intervals = [[1,3],[6,9]], newInterval = [1,4])
print Solution().insert(intervals = [[1,3],[6,9]], newInterval = [1,2])
print Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
print Solution().insert(intervals = [[0,0],[6,9]], newInterval = [1,2])
print Solution().insert(intervals = [[1,1],[6,9]], newInterval = [0,0])
print Solution().insert(intervals = [[1,1],[6,9]], newInterval = [0,1])
