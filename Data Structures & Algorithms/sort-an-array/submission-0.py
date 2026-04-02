from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: a list of length 0 or 1 is already sorted
        if len(nums) <= 1:
            return nums
        
        # Split
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # Merge and return
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0
        
        # Merge the two sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Append any leftovers
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])
        
        return merged
