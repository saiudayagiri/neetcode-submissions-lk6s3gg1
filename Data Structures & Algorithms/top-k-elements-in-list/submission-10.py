class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
        res = []
        heap = []
        for num,cnt in hm.items():
            heapq.heappush(heap,(cnt,num))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        