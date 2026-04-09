class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        def bct(i,curxor):
            nonlocal res
            if i==len(nums):
                res+=curxor
                return
            bct(i+1,curxor^nums[i])
            bct(i+1,curxor)
            return
        bct(0,0)
        return res
        