class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm=Counter(nums)
        nums.sort(key=lambda n:(hm[n],-n))
        return nums
        