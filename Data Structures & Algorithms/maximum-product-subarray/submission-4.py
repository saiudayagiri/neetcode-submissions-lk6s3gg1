class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        minsub=1
        maxsub=1
        for num in nums:
            temp=maxsub*num
            maxsub=max(temp,minsub*num,num)
            minsub=min(temp,minsub*num,num)
            maxi=max(maxsub,minsub,maxi)
        return maxi    
        