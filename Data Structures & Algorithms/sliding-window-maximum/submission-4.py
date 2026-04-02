class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=deque()
        res=[]
        for i in range(len(nums)):
            while stack and stack[0]<i-k+1:
                stack.popleft()
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            stack.append(i)
            if i>=k-1:
                res.append(nums[stack[0]])
        return res            



        