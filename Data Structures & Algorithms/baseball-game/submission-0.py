class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for c in operations:
            if c=="C":
                if stack:
                    stack.pop()
            elif c=="+":
                num1=stack[-1]
                num2=stack[-2]
                stack.append(num1+num2)
            elif c=="D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(c))
        return sum(stack)
        