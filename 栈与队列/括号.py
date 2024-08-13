from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(l+r)
            elif tokens[i] == '-':
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(l-r)
            elif tokens[i] == '*':
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(l*r)
            elif tokens[i] == '/':
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(int(l/r))
            else:
                stack.append(tokens[i])
        return int(stack.pop())
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() is not s[i]:
                    return False
        if stack:
            return False
        return True
                
s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.isValid('[](){}'))