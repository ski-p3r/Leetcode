class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=list(word1)
        n=1
        k=0
        for i in word2:
            l.insert(n+k, i)
            k+=1
            n+=1
        
        return ''.join(l)