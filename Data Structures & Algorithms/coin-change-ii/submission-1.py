class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def func(i,tot,memo):
            if (i,tot) in memo:
                return memo[(i,tot)]
            if tot==amount:
                return 1
            if tot>amount or i==len(coins):
                return 0
            include=func(i,tot+coins[i],memo)
            skip=func(i+1,tot,memo)
            memo[(i,tot)]=include+skip        
            return memo[(i,tot)]
        return func(0,0,{})    
        