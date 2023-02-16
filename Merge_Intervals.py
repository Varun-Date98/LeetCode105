from typing import List

'''
56. Merge Intervals | Medium
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals
and return an array of the non-overlapping intervals that cover all the intervals in the input.
------------------------------------------------------------------------------------------------

'''


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    res, i = [], 0
    intervals.sort(key=lambda x: x[0])

    while i < len(intervals):
        if not res or res[-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            x, y = res.pop()
            a, b = intervals[i]
            res.append([x, max(y, b)])
        
        i += 1
    
    return res
