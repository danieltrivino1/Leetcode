# 71. Simplify Path
# Solution 1 (stack):
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        print(path)
        for element in path:
            if stack and element == '..':
                stack.pop()
            elif element != '..' and element != '.' and element != '':
                stack.append(element)
        stack = '/' + '/'.join(stack)
        return stack
# Solution 2 (stack):
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for element in path.split('/'):
            if element == '..':
                if stack:
                    stack.pop()
            elif element == '.' or not element:
                continue
            else:
                stack.append(element)
        return '/' + '/'.join(stack)
