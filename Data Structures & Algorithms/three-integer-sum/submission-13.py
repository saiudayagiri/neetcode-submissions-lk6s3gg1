class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if num1 + nums[l] + nums[r] == 0:
                    res.append([num1,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                    
                    
                elif num1 + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res

        