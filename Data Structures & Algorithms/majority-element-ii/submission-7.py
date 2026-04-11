class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize candidates with values that won't interfere 
        # (None is safer than -1 since -1 could be a valid element)
        num1, num2 = -1, -1
        cnt1, cnt2 = 0, 0
        
        # Phase 1: Finding potential candidates
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        # Phase 2: Verification
        # Reset counts to strictly count the occurrences of candidates
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)
            
        return res