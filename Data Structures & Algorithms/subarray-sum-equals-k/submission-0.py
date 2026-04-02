class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        cursum=0
        hm={0:1}
        for num in nums:
            cursum+=num
            res+=hm.get(cursum-k,0)
            hm[cursum]=hm.get(cursum,0)+1
        return res
        