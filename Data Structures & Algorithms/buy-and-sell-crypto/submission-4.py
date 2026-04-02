class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0      # buy day
        maxp = 0

        for r in range(1, len(prices)):  # sell day
            if prices[r] > prices[l]:
                maxp = max(maxp, prices[r] - prices[l])
            else:
                l = r   # new minimum price

        return maxp
