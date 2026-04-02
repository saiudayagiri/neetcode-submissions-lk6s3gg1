class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=deque()
        res=[]
        for i in range(len(nums)):
            if stack and i-k+1>stack[0]:
                stack.popleft()
            while stack and nums[i]>nums[stack[-1]]:
                stack.pop()
            stack.append(i)    
            if i>=k-1:
                res.append(nums[stack[0]])   
        return res         

        