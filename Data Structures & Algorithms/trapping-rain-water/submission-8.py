class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = 0
        rmax = 0
        res = 0
        while l <= r:
            if height[l] <= height[r]:
                lmax = max(lmax,height[l])
                res += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                res += rmax - height[r]
                r -= 1
        return res

        