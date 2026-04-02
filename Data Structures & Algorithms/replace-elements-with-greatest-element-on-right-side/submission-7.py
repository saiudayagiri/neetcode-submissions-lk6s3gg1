class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*len(arr)
        maxsofar=-1
        for i in range(len(arr)-1,-1,-1):
            res[i]=maxsofar
            maxsofar=max(maxsofar,arr[i])
        return res

        