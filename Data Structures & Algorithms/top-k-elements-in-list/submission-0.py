class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]  # Frequency buckets
        
        for num, freq in count.items():
            bucket[freq].append(num)  # Store numbers by frequency
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):  # Traverse from high to low frequency
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result