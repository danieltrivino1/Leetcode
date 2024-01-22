# 1208. Get Equal Substrings Within Budget
# Solution (slidding window):
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        cum_cost = 0
        ans = 0
        s = list(s)
        t = list(t)
        for right in range(len(s)):
            cum_cost += abs(ord(s[right]) - ord(t[right]))
            while cum_cost > maxCost:
                cum_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
      
