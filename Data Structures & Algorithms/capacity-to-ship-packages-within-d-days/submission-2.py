class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacity(w):
            curweight=0
            days=1
            for num in weights:
                if curweight+num>w:
                    days+=1
                    curweight=num
                else:
                    curweight+=num
            return days
        l=max(weights)
        r=sum(weights)
        res = sum(weights)
        while l<=r:
            m=r-(r-l)//2
            if capacity(m)<=days:
                res=m
                r=m-1
            else:
                l=m+1
        return res
        