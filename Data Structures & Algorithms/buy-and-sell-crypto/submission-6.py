class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=prices[0]
        for num in prices:
            maxi=max(maxi,num-mini)
            mini=min(mini,num)
        return maxi

        