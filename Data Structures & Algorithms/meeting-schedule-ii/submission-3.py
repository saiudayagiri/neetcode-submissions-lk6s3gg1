"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts=[]
        ends=[]
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        cnt=0
        maxrooms=0
        p1=0
        p2=0
        while p1<len(intervals):
            if starts[p1]<ends[p2]:
                cnt+=1
                p1+=1
            else:
                cnt-=1
                p2+=1
            maxrooms=max(maxrooms,cnt)
        return maxrooms
        