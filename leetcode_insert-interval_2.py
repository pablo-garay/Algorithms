class Solution:  #Beats 100.00%
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval] 

        (start1, end1) = newInterval
        was_added = False
        res = []

        if end1 < intervals[0][0]:
            return [newInterval] + intervals

        if start1 > intervals[-1][1]:
            return intervals + [newInterval]


        i = 0
        while i < len(intervals):
            start2, end2 = intervals[i]

            if was_added:
                res.append([start2, end2])

            elif end1 < start2:
                res.append([start1, end1])
                res.append([start2, end2])
                was_added = True
            
            elif start1 > end2:
                res.append([start2, end2])
            
            else:
                start1, end1 = (min(start1, start2), max(end1, end2))
                
                while i + 1 < len(intervals) and end1 >= intervals[i + 1][0]:
                    start2, end2 = intervals[i + 1]
                    start1, end1 = (min(start1, start2), max(end1, end2))
                    i += 1

                res.append([start1, end1])
                was_added = True

            i += 1       

        if not was_added:
            res.append([start1, end1])
            was_added = True
        
        return res
