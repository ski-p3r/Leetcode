class Solution:
    def addDigits(self, num: int) -> int:
        s=sum([int(i) for i in str(num)])
        while len(str(s))>1:
            s=sum([int(i) for i in str(s)])
        return s
        