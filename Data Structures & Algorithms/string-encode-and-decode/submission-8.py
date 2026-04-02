class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for string in strs:
            res+= str(len(string))+"#"+string
        return res


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        n=len(s)
        while i<n:
            j=i
            while j<n and s[j]!="#":
                j+=1
            lent=int((s[i:j]))
            res.append(s[j+1:j+1+lent])
            i=j+1+lent
        return res


