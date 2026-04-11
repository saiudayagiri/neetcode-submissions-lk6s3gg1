class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Data Cleanse
        # We only care about numbers in range [1, n]. 
        # Anything else is 'noise' and can be set to n + 1.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # 2. Marking Presence
        # Use the value as an index and negate the value at that index.
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                # We use (val - 1) because the array is 0-indexed
                # But we only negate it if it's currently positive
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        
        # 3. Find the first positive index
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all indices 0 to n-1 are negative, then 1...n are present.
        return n + 1