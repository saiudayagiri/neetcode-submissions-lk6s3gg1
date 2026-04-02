class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        cnt=[0]*100001
        for num in nums:
            cnt[num+50000]+=1
        res=[]
        for i in range(len(cnt)):
            res.extend([i-50000]*cnt[i])
        return res
        