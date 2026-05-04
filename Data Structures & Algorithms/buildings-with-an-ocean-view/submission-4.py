class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_so_far = 0
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_so_far:
                max_so_far = heights[i]
                res.append(i)
        return sorted(res)
        