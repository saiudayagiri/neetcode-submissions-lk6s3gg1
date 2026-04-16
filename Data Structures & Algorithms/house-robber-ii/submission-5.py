class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo = {}
        def dfs(i,nums,idd):
            if (i,idd) in memo:
                return memo[(i,idd)]
            if i >=len(nums):
                return 0
            memo[(i,idd)]=max(dfs(i+1,nums,idd),dfs(i+2,nums,idd)+nums[i])
            return memo[(i,idd)]
        return max(dfs(0,nums[:len(nums)-1],0),dfs(0,nums[1:],1))

        