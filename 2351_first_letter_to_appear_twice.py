# 2351. First Letter to Appear Twice
# Solution 1 (Hash map):
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dic = {}
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
            if dic[letter] == 2:
                return letter

# Solution 2 (set):
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for l in s:
            if l in seen:
                return l
            else:
                seen.add(l)
              
