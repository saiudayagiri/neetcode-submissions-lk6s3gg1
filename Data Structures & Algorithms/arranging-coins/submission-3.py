class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            m=r-(r-l)//2
            if m*(m+1)//2 >n:
                r=m-1
            else:
                l=m+1
        return r
        