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
# Solution (stack and dictionary):
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in parenthesis:
                if stack and stack[-1] == parenthesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
