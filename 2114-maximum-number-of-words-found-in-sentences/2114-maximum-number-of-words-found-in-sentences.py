class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=[]
        for i in sentences:
            t=len(i.split())
            l.append(t)
        return max(l)