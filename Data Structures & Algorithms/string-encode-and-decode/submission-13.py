class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            res+= str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        l=0
        r=0
        res=[]
        while l<len(s):
            
            while r<len(s) and s[r]!="#":
                r+=1
            lent=int(s[l:r])
            res.append(s[r+1:r+1+lent])
            l=r+1+lent
            r=l
        return res

