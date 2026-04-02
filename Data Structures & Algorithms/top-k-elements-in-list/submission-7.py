class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
        res=sorted(hm.keys(),key=lambda x:-hm[x])
        return res[:k]
        