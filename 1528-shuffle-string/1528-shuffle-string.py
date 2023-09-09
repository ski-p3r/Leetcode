class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sortedList=sorted(indices)
        k=[]
        for i in sortedList:
            j=indices.index(i)
            k.append(s[j])
        return ''.join(k)