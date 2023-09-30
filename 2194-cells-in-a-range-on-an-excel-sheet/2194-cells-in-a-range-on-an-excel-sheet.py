class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        k=s.split(':')
        l=int(k[-1][-1])
        first=int(k[0][-1])
        kk=[]
        for i in range(ord(k[0][0]), ord(k[-1][0])+1):
            for j in range(first,l+1):
                kk.append(str(chr(i)+str(j)))
        return kk
            