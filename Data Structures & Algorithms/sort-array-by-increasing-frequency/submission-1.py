from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 1. Count frequencies
        hm = Counter(nums)
        n = len(nums)
        
        # 2. Create buckets. Use range to ensure distinct list objects.
        # Index 0 is unused because a frequency must be at least 1.
        cnt = [[] for _ in range(n + 1)]
        
        # 3. Map hm to cnt: index is the count, value is the number
        for val, freq in hm.items():
            cnt[freq].append(val)
            
        res = []
        # 4. Iterate through buckets (1 to n)
        for freq in range(1, n + 1):
            if cnt[freq]:
                # Requirement: If frequencies are the same, sort values descending
                cnt[freq].sort(reverse=True)
                
                for num in cnt[freq]:
                    # Add 'num' to the result 'freq' times
                    res.extend([num] * freq)
                    
        return res