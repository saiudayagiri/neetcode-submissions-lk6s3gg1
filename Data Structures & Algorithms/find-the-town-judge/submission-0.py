class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts=[0]*(n+1)
        trustby=[0]*(n+1)
        for t in trust:
            trusts[t[0]]=1
            trustby[t[1]]+=1
        for i in range(n+1):
            if trusts[i]==0 and trustby[i]==n-1:
                return i
        return -1
        