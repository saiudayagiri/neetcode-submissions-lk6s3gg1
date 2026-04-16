class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        prevend=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=prevend:
                prevend = intervals[i][1]
            else:
                res+=1
                prevend=min(prevend,intervals[i][1])
        return res
        