from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = defaultdict(int)
        
        # Phase 1: Candidate Generation
        for num in nums:
            counts[num] += 1
            
            # If we have more than 2 potential candidates (k-1)
            if len(counts) > 2:
                # Decrement all current candidates
                # Note: We must create a list of keys because we'll modify the dict
                for key in list(counts.keys()):
                    counts[key] -= 1
                    if counts[key] == 0:
                        del counts[key]
        
        # Phase 2: Verification
        # The map now contains at most 2 potential candidates
        res = []
        for candidate in counts:
            # We must recount from the original array to ensure 
            # they actually meet the > n/3 threshold
            actual_count = 0
            for num in nums:
                if num == candidate:
                    actual_count += 1
            
            if actual_count > n // 3:
                res.append(candidate)
                
        return res