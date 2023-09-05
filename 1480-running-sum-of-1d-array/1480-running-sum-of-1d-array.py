class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            n=0
            for j in range(i+1):
                n+=nums[j]
            l.append(n)
        return l