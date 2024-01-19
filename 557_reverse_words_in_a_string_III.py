# 557. Reverse Words in a String III
# Solution (two pointers):
class Solution:
    def reverseWords(self, s: str) -> str:

        result = []
        words = s.split(' ')
        for w in words:
            left = 0
            right = len(w) - 1
            w = list(w)
            while left < right:
                temp = w[left]
                w[left] = w[right]
                w[right] = temp
                left += 1
                right -= 1
            result.append(''.join(w))
        result = ' '.join(result)
        return result
