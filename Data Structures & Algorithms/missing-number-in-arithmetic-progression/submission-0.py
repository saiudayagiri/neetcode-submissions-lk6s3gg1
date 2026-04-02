class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        d = (arr[-1] - arr[0]) // n

        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            expected = arr[0] + m * d

            if arr[m] == expected:
                # left side is perfect, missing is on right
                l = m + 1
            else:
                # mismatch found, missing is on left
                r = m - 1

        # missing value is what should be at index l
        return arr[0] + l * d
