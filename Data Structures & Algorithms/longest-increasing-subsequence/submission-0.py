class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, prev):
            if i == len(nums):
                return 0
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i+1, i)
            not_take = dfs(i+1, prev)
            return max(take, not_take)
    
        return dfs(0, -1)
                
        