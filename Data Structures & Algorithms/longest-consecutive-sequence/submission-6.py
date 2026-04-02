class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        res=0
        for num in nums:
            if num-1 not in numsset:
                cnt=1
                while num+cnt in numsset:
                    cnt+=1
                res=max(res,cnt)
        return res
        