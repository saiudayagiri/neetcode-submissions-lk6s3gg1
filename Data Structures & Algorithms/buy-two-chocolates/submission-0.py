class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1=float("inf")
        min2=float("inf")
        for num in prices:
            if num<min1:
                min2=min1
                min1=num
            elif num<min2:
                min2=num
        return money-min1-min2 if money-min1-min2 >=0 else money
        