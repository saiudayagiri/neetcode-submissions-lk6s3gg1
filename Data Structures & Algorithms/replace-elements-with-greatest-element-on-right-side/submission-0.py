class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxsofar=-1
        res=[-1]*len(arr)
        for i in range(len(arr)-1,-1,-1):
            res[i]=maxsofar
            maxsofar=max(maxsofar,arr[i])
        return res

        