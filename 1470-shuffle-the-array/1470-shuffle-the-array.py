class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s,y=nums[:n],nums[n:]
        f=[]
        for i in range(len(s)):
            f.append(s[i])                    
            f.append(y[i])        
        return f