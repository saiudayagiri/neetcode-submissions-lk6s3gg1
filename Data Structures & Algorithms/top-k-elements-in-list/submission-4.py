class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=sorted(count.items(),key=lambda x:-x[1])
        return [num for num,cnt in res[:k]]