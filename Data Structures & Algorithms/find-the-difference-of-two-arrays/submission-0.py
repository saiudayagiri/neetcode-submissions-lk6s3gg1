class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1set=set(nums1)
        nums2set=set(nums2)
        res=[[],[]]
        for num in nums1set:
            if num not in nums2set:
                res[0].append(num)
        for num in nums2set:
            if num not in nums1set:
                res[1].append(num)
        return res

        