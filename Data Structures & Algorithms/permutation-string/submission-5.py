class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        hm1={}
        hm2={}
        for i in range(len(s1)):
            hm1[s1[i]]=hm1.get(s1[i],0)+1
            hm2[s2[i]]=hm2.get(s2[i],0)+1
        for i in range(len(s1),len(s2)):
            if hm1==hm2:
                return True
            hm2[s2[i]]=hm2.get(s2[i],0)+1
            hm2[s2[i-len(s1)]]-=1
            if hm2[s2[i-len(s1)]] == 0:
                del hm2[s2[i-len(s1)]]
        return hm1==hm2
        