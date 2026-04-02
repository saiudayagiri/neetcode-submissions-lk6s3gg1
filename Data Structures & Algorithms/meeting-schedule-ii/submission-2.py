"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ends=[]
        starts=[]
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        ends.sort()
        starts.sort()
        i,j=0,0
        mx=0
        rooms=0
        while i<len(starts):
            if starts[i]<ends[j]:
                rooms+=1
                i+=1
            else:
                rooms-=1
                j+=1
            mx=max(rooms,mx) 
        return mx               
        