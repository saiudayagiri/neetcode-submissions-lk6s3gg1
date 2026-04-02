class Solution:
    def isHappy(self, n: int) -> bool:
        vis=set()
        while n not in vis:
            vis.add(n)
            n=self.helper(n)
            if n==1:
                return True
        return False
    def helper(self,n:int)-> int:
        out=0
        while n:
            di=n%10
            di=di**2
            out+=di
            n=n//10
        return out    
