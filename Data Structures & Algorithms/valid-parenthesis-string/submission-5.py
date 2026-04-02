class Solution:
    def checkValidString(self, s: str) -> bool:
        minopen = 0
        maxopen = 0
        
        for c in s:
            if c == "(":
                minopen += 1
                maxopen += 1
            elif c == ")":
                minopen -= 1
                maxopen -= 1
            else:  # '*' can be either '(' or ')'
                minopen -= 1  # '*' can act as ')'
                maxopen += 1  # '*' can act as '('

            if maxopen < 0:
                return False 
            if minopen<0:
                minopen=0
                     # Too many closing brackets.

        # At the end, we can only have a valid string if minopen <= 0
        return minopen == 0
        