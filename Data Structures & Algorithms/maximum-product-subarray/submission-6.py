class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        minsub=nums[0]
        maxsub=nums[0]
        for num in nums[1:]:
            temp=maxsub*num
            maxsub=max(temp,minsub*num,num)
            minsub=min(temp,minsub*num,num)
            maxi=max(maxsub,minsub,maxi)
        return maxi    
        