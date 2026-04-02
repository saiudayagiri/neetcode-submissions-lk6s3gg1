class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        prof=0
        for num in prices:
            mini=min(num,mini)
            prof=max(prof,num-mini)
        return prof    
        