class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm=Counter(nums)
        res = []
        freq = [[] for i in range(len(nums)+1)]
        for key,cnt in hm.items():
            freq[cnt].append(key)
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
                    

        