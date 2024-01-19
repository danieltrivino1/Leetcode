# 917. Reverse Only Letters
# Solution (two pointers):
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1  
            elif not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
        s = ''.join(s)
        return s
