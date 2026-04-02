class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        setnums1=set(nums1)
        res=set()
        for num in nums2:
            if num in setnums1:
                res.add(num)
        return list(res)
            
        