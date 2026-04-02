class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def xor_of_all(index, current_xor):
            # Base case: if we've reached the end of the list
            if index == len(nums):
                return current_xor
            
            # We add the results of the two branching paths:
            # 1. Including the current number in the XOR sum
            # 2. Excluding the current number from the XOR sum
            return xor_of_all(index + 1, current_xor ^ nums[index]) + \
                   xor_of_all(index + 1, current_xor)

        # Start the recursion from index 0 with an initial XOR sum of 0
        return xor_of_all(0, 0)