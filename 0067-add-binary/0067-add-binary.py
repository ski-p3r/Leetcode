class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=int(a, 2)+int(b,2)
        return str(bin(i)[2:])