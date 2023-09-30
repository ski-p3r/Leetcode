class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list1 = s.split()
        return " ".join(list1[:k])
        