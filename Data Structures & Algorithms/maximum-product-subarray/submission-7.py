class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxsub=nums[0]
        minsub=nums[0]
        maxi=nums[0]
        for num in nums[1:]:
            temp = maxsub*num
            maxsub=max(maxsub*num,minsub*num,num)
            minsub=min(temp,minsub*num,num)
            maxi=max(maxi,maxsub,minsub)
        return maxi
        