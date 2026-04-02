class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count=Counter(s1)
        s2count={}
        i=0
        for r in range(len(s2)):
            s2count[s2[r]]=s2count.get(s2[r],0)+1
            if r-i+1>len(s1):
                s2count[s2[i]]-=1
                if s2count[s2[i]]<=0:
                    del s2count[s2[i]]
                i+=1
            if s2count==s1count:
                return True
        return False            

        