class Solution:
    def isMajorityElement(self, nums, target):
        n = len(nums)

        # find leftmost occurrence
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        left = l

        # if target not present
        if left == n or nums[left] != target:
            return False

        # find rightmost occurrence
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        right = r

        return (right - left + 1) > n // 2
