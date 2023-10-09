class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            return word.replace(word[:word.index(ch)+1], word[:word.index(ch)+1][::-1])
        return word
        