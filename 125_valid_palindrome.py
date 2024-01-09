# 125. Valid Palindrome
# Solution 1 (two pointers):
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            while (not s[left].isalnum() or s[left] == ' ') and (left < right):
                left += 1
            while (not s[right].isalnum() or s[right] == ' ') and (left < right):
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
# Solution 2 (two pointers):
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        
