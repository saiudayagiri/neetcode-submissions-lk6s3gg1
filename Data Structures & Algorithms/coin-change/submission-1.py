class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i, rem):
            if (i,rem) in memo:
                return memo[(i,rem)]
            # Base Case: We hit the target exactly
            if rem == 0:
                return 0
            
            # Base Case: Out of bounds or went over the amount
            if i >= len(coins) or rem < 0:
                return float('inf')
            
            # Choice 1: INCLUDE the current coin (coins[i])
            # We stay at index 'i' because we can reuse this coin
            res_include = dfs(i, rem - coins[i])
            if res_include != float('inf'):
                res_include += 1 # Add 1 to represent using this coin
                
            # Choice 2: EXCLUDE the current coin and move on
            res_exclude = dfs(i + 1, rem)
            
            memo[(i,rem)] = min(res_include, res_exclude)
            return memo[(i,rem)]

        result = dfs(0, amount)
        return result if result != float('inf') else -1
        