class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={"}":"{","]":"[",")":"("}
        for c in s:
            if c in hm:
                if stack and hm[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0                
        