"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals):  # Time: O(n log n)
        intervals = [(interval.start, interval.end) for interval in intervals]
        intervals.sort(key=lambda x: (x[0], x[1]))  # O(n log n)

        for i in xrange(len(intervals) - 1):  # O(n)
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


print Solution().canAttendMeetings(intervals = [(0,30),(5,10),(15,20)])
print Solution().canAttendMeetings(intervals = [(5,8),(9,15)])
