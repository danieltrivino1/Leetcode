# 1832. Check if the Sentence Is Pangram
# Solution (set):
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set(sentence)
        for letter in sentence:
            if not letter.isalpha():
                sentence.discard(letter)
        if len(sentence) == 26:
            return True
        else:
            return False
          
