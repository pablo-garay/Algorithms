"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted([(interval.start, interval.end) for interval in intervals])
        intervals.sort(key=lambda x: (x[0], x[1]))

        for i in xrange(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


print Solution().canAttendMeetings(intervals = [(0,30),(5,10),(15,20)])
print Solution().canAttendMeetings(intervals = [(5,8),(9,15)])
