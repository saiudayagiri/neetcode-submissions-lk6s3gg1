class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            m=(l+r)//2
            if m*(m+1)//2 < n:
                l=m+1
            elif m*(m+1)//2 > n:
                r=m-1
            else:
                return m
        return r