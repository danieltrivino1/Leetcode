# 202. Happy Number
# Solution (one pointer and set):
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n != 1 and n not in seen):
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return True if n == 1 else False
