class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        for num in prices:
            mini = min(num,mini)
            if num > mini:
                profit += num - mini
                mini = num
        return profit
        