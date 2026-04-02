class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        offset = 50000
        arr = [0] * 100001
        for num in nums:
            arr[num+offset]+=1
        res=[]
        for i in range(len(arr)):
            res.extend([i-50000]*arr[i])
        return res
        