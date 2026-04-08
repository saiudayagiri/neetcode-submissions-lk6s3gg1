class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n) # We found a pair!
            else:
                seen.add(n)    # Waiting for a partner...
        
        return len(seen) == 0