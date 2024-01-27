# 844. Backspace String Compare
# Solution 1 (stack):
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t =[]

        for letter_s in s:
            if stack_s and letter_s == '#':
                stack_s.pop()
            elif letter_s != '#':
                stack_s.append(letter_s)

        for letter_t in t:
            if stack_t and letter_t == '#':
                stack_t.pop()
            elif letter_t != '#':
                stack_t.append(letter_t)
        
        return stack_s == stack_t

# Solution 2 (stack):
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(string):
            stack = []
            for letter in string:
                if letter != '#':
                    stack.append(letter)
                elif stack:
                    stack.pop()
            return stack
        return build_stack(s) == build_stack(t)
