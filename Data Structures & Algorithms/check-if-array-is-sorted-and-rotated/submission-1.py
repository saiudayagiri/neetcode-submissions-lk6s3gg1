class Solution:
    def check(self, nums: List[int]) -> bool:
        l=0
        n=len(nums)
        for i in range(1,2*n):
            if nums[i%n]<nums[(i-1)%n]:
                l=i
            if i-l+1==n:
                return True
        return False
        