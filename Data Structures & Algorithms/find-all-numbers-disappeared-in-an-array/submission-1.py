class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx= abs(num)-1
            nums[idx]=-1*abs(nums[idx])
        cnt=0
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
        