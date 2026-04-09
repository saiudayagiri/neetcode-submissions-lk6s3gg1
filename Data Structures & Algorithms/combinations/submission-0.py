class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
        
        for i in range(1,n+1):
            arr.append(i)
        res=[]
        def bct(i,curarr):
            nonlocal res
            if len(curarr[:])==k:
                res.append(curarr[:])
                return
            if i==len(arr):
                return
            curarr.append(arr[i])
            bct(i+1,curarr)
            curarr.pop()
            bct(i+1,curarr)
            return
        bct(0,[])
        return res
        