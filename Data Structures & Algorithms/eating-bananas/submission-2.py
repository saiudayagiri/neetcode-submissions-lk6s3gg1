class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            res=0
            for pile in piles:
                if pile%k:
                    res+= (pile//k) + 1
                else:
                    res+= pile//k
            return res
        l=1
        r=max(piles)
        res=0
        while l<=r:
            m=r-(r-l)//2
            if hours(m)<=h:
                res=m
                r=m-1
            else:
                l=m+1
        return res

        