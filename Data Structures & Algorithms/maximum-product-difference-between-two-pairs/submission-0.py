class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxi1=0
        maxi2=0
        mini1=float("inf")
        mini2=float("inf")
        for num in nums:
            if num>maxi1:
                maxi2=maxi1
                maxi1=num
            elif num >maxi2:
                maxi2=num
            
            if num<mini1:
                mini2=mini1
                mini1=num
            elif num<mini2:
                mini2=num
        return maxi1*maxi2-mini1*mini2
        