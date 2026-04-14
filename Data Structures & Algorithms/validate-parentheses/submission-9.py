class Solution:
    def isValid(self, s: str) -> bool:
        hm={")":"(","]":"[","}":"{"}
        stack=[]
        for c in s:
            if c in "({[" :
                stack.append(c)
            elif stack and hm[c]==stack[-1]:
               
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True 
        