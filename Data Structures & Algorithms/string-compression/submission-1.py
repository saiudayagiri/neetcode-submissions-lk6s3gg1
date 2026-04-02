class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        j=0
        for r in range(len(chars)+1):
            if r==len(chars) or chars[r]!=chars[i]:
                chars[j]=chars[i]
                j+=1
                if r-i>1:
                    for c in str(r-i):
                        chars[j]=c
                        j+=1
                i=r
        return j
             

        