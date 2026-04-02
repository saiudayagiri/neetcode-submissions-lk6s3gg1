class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm=Counter(nums)
        res=set()
        for num in nums:
            if hm[num]>len(nums)//3:
                res.add(num)
        return list(res)


        