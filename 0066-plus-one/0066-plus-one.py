class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        d=int(s)+1
        h=[]
        for i in str(d):
            h.append(int(i))
        return h
        