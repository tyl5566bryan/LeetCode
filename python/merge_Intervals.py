# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        
        intervals.sort(key = lambda x: x.start)
        
        res, left, right = [], intervals[0].start, intervals[0].end
        
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= right:
                right = max(right, intervals[i].end)
            else:
                res.append(Interval(left, right))
                left, right = intervals[i].start, intervals[i].end
        
        res.append(Interval(left, right))
        
        return res
