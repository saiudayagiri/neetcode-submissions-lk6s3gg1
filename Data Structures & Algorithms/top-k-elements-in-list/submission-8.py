class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
        sor= sorted(hm.keys(),key=lambda x:-hm[x])
        return sor[:k]
        