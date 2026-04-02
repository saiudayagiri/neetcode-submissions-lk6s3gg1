class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hm={')':'(','}':'{',']':'['}
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack and hm[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
        