class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        r = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r-k+1 > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])


        return output