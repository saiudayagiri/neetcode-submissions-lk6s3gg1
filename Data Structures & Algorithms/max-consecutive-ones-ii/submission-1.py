class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        z=0
        maxi=0
        for r in range(len(nums)):
            if nums[r]==0:
                z+=1
            while z>1:
                if nums[l]==0:
                    z-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
        