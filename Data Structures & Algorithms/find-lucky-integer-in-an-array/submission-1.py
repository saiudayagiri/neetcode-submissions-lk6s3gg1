class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # find max value to size frequency array
        max_val = max(arr)
        freq = [0] * (max_val + 1)

        # count frequencies
        for num in arr:
            freq[num] += 1

        # check from largest to smallest
        for num in range(max_val, 0, -1):
            if freq[num] == num:
                return num
        return -1
