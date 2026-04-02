class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)
        for num,cnt in count.items():
            if cnt>len(nums)//3:
                res.append(num)
        return res
        
        