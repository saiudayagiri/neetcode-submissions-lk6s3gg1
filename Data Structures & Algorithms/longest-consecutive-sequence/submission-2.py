class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        res=0
        for num in nums:
            if num-1 not in numsset:
                length=1
                while num+length in numsset:
                    length+=1
                res=max(res,length)
        return res        


        