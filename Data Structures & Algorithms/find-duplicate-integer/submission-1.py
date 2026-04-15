class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # 1. Get the index this value "points" to
            index = abs(nums[i]) - 1
            
            # 2. Check if we have visited this index before
            if nums[index] < 0:
                # If it's already negative, abs(nums[i]) is our duplicate!
                return abs(nums[i])
            
            # 3. Mark the destination as visited by making it negative
            nums[index] = -nums[index]
            
        return -1 # Should not happen per problem constraints