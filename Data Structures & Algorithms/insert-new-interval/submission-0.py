class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals,key = lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        return res
        