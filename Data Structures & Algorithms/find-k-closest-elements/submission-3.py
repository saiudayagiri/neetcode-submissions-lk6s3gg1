class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = 0
        r = len(arr) - 1
        
        # Keep shrinking the window from whichever side is further from x
        while r - l + 1 > k:
            # Check which end is further from x
            # Use <= because if distances are equal, the smaller index (left) wins
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
                
        return arr[l:r+1]