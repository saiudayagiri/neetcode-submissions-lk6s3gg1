class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        stack=[]
        for r in range(len(nums)):
            while stack and nums[stack[-1]]<nums[r]:
                stack.pop()
            stack.append(r)
            if stack[0]<r-k+1:
                stack.pop(0)
            if  r>=k-1:
                res.append(nums[stack[0]])  
        return res             

        