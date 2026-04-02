class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        maxi=0
        for num in nums:
            if num-1 in numsset:
                continue
            cur = num
            while cur in numsset:
                cur+=1
            maxi=max(maxi,cur-num)
        return maxi

        