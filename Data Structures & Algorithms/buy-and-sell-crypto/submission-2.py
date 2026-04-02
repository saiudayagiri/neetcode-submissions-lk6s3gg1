class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        mini=prices[0]
        for num in prices:
            maxp=max(maxp,num-mini)
            mini=min(mini,num)
        return maxp
        