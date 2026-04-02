class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm={0:1}
        cursum=0
        res=0
        for num in nums:
            cursum+=num
            res+=hm.get(cursum-k,0)
            hm[cursum]=hm.get(cursum,0)+1
        return res
        