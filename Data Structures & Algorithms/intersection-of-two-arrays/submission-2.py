class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<len(nums2):
            nums1,nums2=nums2,nums1
        nums2set=set(nums2)
        res=set()
        for num in nums1:
            if num in nums2set:
                res.add(num)
        return list(res)
        