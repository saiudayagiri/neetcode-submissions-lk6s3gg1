class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        
        def dfs(i, first_taken):
            if i >= n:
                return 0
            if i == n-1 and first_taken:
                # Cannot take the last house if first house was taken
                return 0
            
            if (i, first_taken) in memo:
                return memo[(i, first_taken)]
            
            # Choice 1: Take nums[i]
            take = nums[i] + dfs(i + 2, first_taken)
            # Choice 2: Skip nums[i]
            skip = dfs(i + 1, first_taken)
            
            memo[(i, first_taken)] = max(take, skip)
            return memo[(i, first_taken)]
        
        if n == 1:
            return nums[0]
        
        return max(
            dfs(0, True),   # start at index 0
            dfs(1, False)   # start at index 1
        )
