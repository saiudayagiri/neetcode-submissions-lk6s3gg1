class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            
            # Case 1: Left side is sorted
            elif nums[m] > nums[l]:
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Case 2: Right side is sorted
            else:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1