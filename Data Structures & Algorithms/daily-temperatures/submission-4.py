class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for r in range(len(temperatures)):
            while stack and temperatures[r]>temperatures[stack[-1]]:
                res[stack[-1]]=r-stack[-1]
                stack.pop()
            stack.append(r)
        return res
        