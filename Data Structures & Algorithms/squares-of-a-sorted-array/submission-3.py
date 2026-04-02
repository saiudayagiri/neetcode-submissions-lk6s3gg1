class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        l=0
        r=len(nums)-1
        j=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[j]=abs(nums[l])**2
                l+=1
            elif abs(nums[l])<=abs(nums[r]):
                res[j]=abs(nums[r])**2
                r-=1
            j-=1
        return res


        