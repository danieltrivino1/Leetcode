# 844. Backspace String Compare
# Solution (stack):
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
