class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=mx=nums[0]
        for num in nums[1:]:
            cur=max(cur+num,num)
            mx=max(mx,cur)
        return mx    
        