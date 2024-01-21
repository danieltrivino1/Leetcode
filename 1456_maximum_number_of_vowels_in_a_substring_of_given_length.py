# 1456. Maximum Number of Vowels in a Substring of Given Length
# Solution (sliding fixed size window):
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = list(s)
        vowels = 'aeiou'
        # Change to list of 1 and 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = 1
            else:
                s[i] = 0

        curr = 0
        for i in range(k):
            curr += s[i]
        
        ans = curr
        for i in range(k, len(s)):
            curr += s[i]
            curr -= s[i-k]
            ans = max(ans, curr)

        return ans
