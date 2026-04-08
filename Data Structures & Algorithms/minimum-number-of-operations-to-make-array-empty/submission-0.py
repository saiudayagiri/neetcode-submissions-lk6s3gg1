from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        
        for count in cnt.values():
            # If any number appears only once, it's impossible to group
            if count == 1:
                return -1
            
            # This single line handles remainders 0, 1, and 2 perfectly:
            # If remainder is 0: count // 3
            # If remainder is 1 or 2: count // 3 + 1
            res += (count + 2) // 3
            
        return res