class Solution:
    def numberOfSteps(self, num: int) -> int:
        k=0
        while num > 0:
            if num%2==0:
                num=num//2
                k+=1
            else:
                num-=1
                k+=1
        return k
                
        