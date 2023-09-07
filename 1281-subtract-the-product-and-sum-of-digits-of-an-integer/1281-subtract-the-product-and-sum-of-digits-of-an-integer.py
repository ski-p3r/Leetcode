class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        d=str(n)
        f=0
        k=1
        for i in d:
            f+=int(i)
            k*=int(i)
        return k-f