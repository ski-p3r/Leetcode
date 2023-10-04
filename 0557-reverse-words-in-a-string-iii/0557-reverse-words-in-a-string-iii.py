class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        l=[]
        for i in d:
            l.append(i[::-1])
        return ' '.join(l)
        