class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=s.strip().split()
        return len(d[-1])
        