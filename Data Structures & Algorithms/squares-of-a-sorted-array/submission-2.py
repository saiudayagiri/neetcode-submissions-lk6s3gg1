class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        res=[0]*len(nums)
        p=len(nums)-1
        while l<=r:
            if nums[l]*nums[l]>=nums[r]*nums[r]:
                res[p]=nums[l]*nums[l]
                p-=1
                l+=1
            else:
                res[p]=nums[r]*nums[r]
                p-=1
                r-=1
        return res


        