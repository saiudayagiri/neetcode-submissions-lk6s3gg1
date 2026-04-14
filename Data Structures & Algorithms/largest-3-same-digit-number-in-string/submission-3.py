class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=""
        for i in range(len(num)-2,0,-1):
            if num[i]==num[i-1]==num[i+1]:
                if res=="":
                    res=num[i]*3
                if num[i]>res[0]:
                    res=num[i]*3
        return res

        