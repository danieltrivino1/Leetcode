# 2000. Reverse Prefix of Word
# Solution (two pointers):
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        for idx, letter in enumerate(word):
            if letter == ch:
                left = 0
                right = idx
                while left < right:
                    temp = word[left]
                    word[left] = word[right]
                    word[right] = temp
                    left += 1
                    right -= 1
                word = ''.join(word)
                return word
        word = ''.join(word)
        return word
