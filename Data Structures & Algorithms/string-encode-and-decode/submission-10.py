class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for string in strs:
            res+=str(len(string))+ "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        j=0
        while j<len(s):
            while j<len(s) and s[j]!="#":
                j+=1
            lent=int(s[i:j])
            res.append(s[j+1:j+1+lent])
            i=j+1+lent
            j=i
        return res
            
