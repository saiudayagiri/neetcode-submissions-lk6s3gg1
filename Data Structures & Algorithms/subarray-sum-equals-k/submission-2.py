class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        cursum = 0
        res = 0
        for num in nums:
            cursum += num
            if cursum - k in hashmap:
                res += hashmap[cursum - k]
            
            hashmap[cursum] = 1 + hashmap.get(cursum, 0)
        return res
        