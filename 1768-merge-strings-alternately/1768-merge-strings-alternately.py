class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        for i in range(max(len(word1), len(word2))):
            try:
                l.append(word1[i])
                l.append(word2[i])
            except:
                try:
                    l.append(word2[i])
                except:
                    None
        return ''.join(l)