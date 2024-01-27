# 20. Valid Parentheses
# Solution (stack):
class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        for parantheses in s:
            if parantheses == '(':
                stack.append(')')
            elif parantheses == '{':
                stack.append('}')
            elif parantheses == '[':
                stack.append(']')
            elif len(stack) == 0:
                return False 
            elif stack.pop() != parantheses:
                return False
        if len(stack) == 0:
            return True
        else:
          
