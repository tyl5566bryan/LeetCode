# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def binarySearch(intervals, val, isleft):
            left, right = 0, len(intervals) * 2 - 1
            while left <= right:
                mid = (left + right) / 2
                cur_val = intervals[mid/2].start if mid % 2 == 0 else intervals[mid/2].end
                if cur_val == val:
                    return mid - 1 if isleft else mid + 1
                elif cur_val > val:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return right if isleft else left
            
        pos1 = binarySearch(intervals, newInterval.start, True)
        pos2 = binarySearch(intervals, newInterval.end, False)
        
        if pos1 % 2 == 0 and pos2 % 2 == 0:
            temp = Interval(intervals[pos1/2].start, newInterval.end)
            return intervals[0:pos1/2] + [temp] + intervals[pos2/2:len(intervals)]
        elif pos1 % 2 == 0 and pos2 % 2 == 1:
            temp = Interval(intervals[pos1/2].start, intervals[pos2/2].end)
            return intervals[0:pos1/2] + [temp] + intervals[pos2/2 + 1:len(intervals)]
        elif pos1 % 2 == 1 and pos2 % 2 == 0:
            return intervals[0:pos1/2+1] + [newInterval] + intervals[pos2/2:len(intervals)]
        else:
            temp = Interval(newInterval.start, intervals[pos2/2].end)
            return intervals[0:pos1/2+1] + [temp] + intervals[pos2/2 + 1:len(intervals)]
        
        